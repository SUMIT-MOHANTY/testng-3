from datetime import datetime
from sqlalchemy.orm import Session
from backend.models.policy import Premium, Policy
from backend.crud.policy import deduct_premium
from backend.crud.policy import log_to_ledger

def run_premium_scheduling(db: Session) -> None:
    pending = db.query(Premium).filter(Premium.due_date <= datetime.utcnow(), Premium.paid == False).all()
    for premium in pending:
        deduct_premium(db, premium)
        # Expire policy if end_date passed
        policy = db.query(Policy).filter(Policy.id == premium.policy_id).first()
        if policy and policy.end_date <= datetime.utcnow():
            policy.status = "EXPIRED"
            db.add(policy)
            db.commit()
            log_to_ledger("policy_expired", {"policy_id": policy.id})
