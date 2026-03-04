from datetime import date, timedelta
from sqlalchemy.orm import Session
from . import models, schemas, constants
from backend.audit.ledger import record_entry
import logging

logger = logging.getLogger('insurance')

def create_policy(db: Session, payload: schemas.PolicyCreate) -> models.Policy:
    policy = models.Policy(
        user_id=payload.user_id,
        product_code=payload.product_code,
        status=constants.POLICY_STATUS_ACTIVE,
        start_date=payload.start_date,
    )
    db.add(policy)
    db.commit()
    db.refresh(policy)
    record_entry({"type": "policy_created", "policy_id": policy.id, "user_id": policy.user_id})
    logger.info('Policy created %s', policy.id)
    return policy

def schedule_first_premium(db: Session, policy: models.Policy) -> models.Premium:
    first_due = policy.start_date + timedelta(days=30)
    premium = models.Premium(
        policy_id=policy.id,
        due_date=first_due,
        amount_cents=10000,  # fixed mock amount
    )
    db.add(premium)
    db.commit()
    db.refresh(premium)
    record_entry({"type": "premium_scheduled", "policy_id": policy.id, "premium_id": premium.id})
    logger.info('First premium scheduled for policy %s', policy.id)
    return premium

def get_policy(db: Session, policy_id: int) -> models.Policy | None:
    return db.query(models.Policy).filter(models.Policy.id == policy_id).first()

def get_upcoming_premium(db: Session, policy_id: int) -> models.Premium | None:
    today = date.today()
    return (db.query(models.Premium)
            .filter(models.Premium.policy_id == policy_id, models.Premium.paid == False, models.Premium.due_date >= today)
            .order_by(models.Premium.due_date)
            .first())

def record_claim(db: Session, payload: schemas.ClaimCreate) -> models.Claim:
    claim = models.Claim(
        policy_id=payload.policy_id,
        claim_amount_cents=payload.claim_amount_cents,
        status=constants.CLAIM_STATUS_PENDING,
    )
    db.add(claim)
    db.commit()
    db.refresh(claim)
    record_entry({"type": "claim_filed", "claim_id": claim.id, "policy_id": claim.policy_id})
    logger.info('Claim filed %s', claim.id)
    return claim
