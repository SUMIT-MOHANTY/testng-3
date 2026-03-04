from sqlalchemy.orm import Session
from .models import Claim, ClaimStatus
from datetime import datetime

def create_claim(session: Session, **kwargs):
    claim = Claim(**kwargs)
    session.add(claim)
    session.commit()
    session.refresh(claim)
    return claim

def get_claim(session: Session, claim_id: str):
    return session.query(Claim).filter(Claim.id == claim_id).first()

def update_status(session: Session, claim: Claim, new_status: ClaimStatus):
    claim.status = new_status
    now = datetime.utcnow()
    if new_status == ClaimStatus.VALIDATED:
        claim.validated_at = now
    elif new_status == ClaimStatus.APPROVED:
        claim.approved_at = now
    elif new_status == ClaimStatus.PAID:
        claim.paid_at = now
    session.commit()
    return claim
