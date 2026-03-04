from decimal import Decimal
from uuid import uuid4
from .repo import create_claim, get_claim, update_status
from .models import ClaimStatus
from .errors import ClaimNotFound, DocumentMissing, AmountExceeded, IdempotencyConflict
from backend.events.redis_client import redis
from .ledger import record_event
from .payment import execute_payout

class ClaimService:
    def __init__(self, db_session):
        self.db = db_session

    def _check_idempotency(self, key, claim_id=None):
        stored = redis.get(key)
        if stored:
            stored = stored.decode()
            if claim_id and stored != claim_id:
                raise IdempotencyConflict("Key used for another claim")
            return stored
        return None

    def _set_idempotency(self, key, claim_id):
        redis.set(key, claim_id)

    def submit_claim(self, dto, idem_key):
        existing = self._check_idempotency(idem_key)
        if existing:
            claim = get_claim(self.db, existing)
            return claim
        if dto.amount > Decimal('50000'):
            raise AmountExceeded("Amount exceeds limit")
        claim = create_claim(
            self.db,
            policy_id=dto.policy_id,
            user_id=dto.user_id,
            amount=dto.amount,
            currency=dto.currency,
            idempotency_key=idem_key,
            status=ClaimStatus.SUBMITTED,
        )
        self._set_idempotency(idem_key, str(claim.id))
        record_event(str(claim.id), "SUBMITTED", dto.dict())
        return claim

    def validate_claim(self, claim_id, dto, idem_key):
        claim = get_claim(self.db, claim_id)
        if not claim:
            raise ClaimNotFound
        self._check_idempotency(idem_key, claim_id)
        required = set(claim.documents or []) or set()
        if not set(dto.documents).issuperset(required):
            raise DocumentMissing("Missing required documents")
        update_status(self.db, claim, ClaimStatus.VALIDATED)
        self._set_idempotency(idem_key, claim_id)
        record_event(claim_id, "VALIDATED", dto.dict())
        return claim

    def approve_claim(self, claim_id, dto, idem_key):
        claim = get_claim(self.db, claim_id)
        if not claim:
            raise ClaimNotFound
        self._check_idempotency(idem_key, claim_id)
        update_status(self.db, claim, ClaimStatus.APPROVED)
        self._set_idempotency(idem_key, claim_id)
        record_event(claim_id, "APPROVED", dto.dict())
        return claim

    def payout_claim(self, claim_id, idem_key):
        claim = get_claim(self.db, claim_id)
        if not claim:
            raise ClaimNotFound
        self._check_idempotency(idem_key, claim_id)
        if claim.status != ClaimStatus.APPROVED:
            raise Exception("Claim not approved")
        execute_payout(str(claim.id), claim.amount, claim.currency)
        update_status(self.db, claim, ClaimStatus.PAID)
        self._set_idempotency(idem_key, claim_id)
        record_event(claim_id, "PAID", {})
        return claim
