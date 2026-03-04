from datetime import date
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from . import models, crud, utils, constants
from backend.audit.ledger import record_entry
import logging
logger = logging.getLogger('insurance')

async def run_premium_schedule():
    db: Session = SessionLocal()
    today = date.today()
    premiums = db.query(models.Premium).filter(models.Premium.paid == False, models.Premium.due_date <= today).all()
    for premium in premiums:
        policy = db.query(models.Policy).filter(models.Policy.id == premium.policy_id).first()
        if not policy:
            continue
        success = utils.debit_user(policy.user_id, premium.amount_cents)
        if success:
            premium.paid = True
            from datetime import datetime
            premium.paid_at = datetime.utcnow()
            policy.status = constants.POLICY_STATUS_ACTIVE
            db.add_all([premium, policy])
            db.commit()
            record_entry({"type": "premium_deduction", "policy_id": policy.id, "premium_id": premium.id, "amount_cents": premium.amount_cents})
            logger.info('Premium %s deducted for policy %s', premium.id, policy.id)
    db.close()
