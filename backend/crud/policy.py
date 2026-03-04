import os
import requests
from datetime import datetime
from decimal import Decimal
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.models.policy import Policy, Premium, Claim
from backend.schemas.policy import PolicyCreate, ClaimCreate

def log_to_ledger(action: str, details: dict):
    # Placeholder for ledger integration - currently just prints
    print(f"LEDGER - {action}: {details}")

def create_policy(db: Session, obj_in: PolicyCreate) -> Policy:
    allowed = ["HOME", "AUTO", "HEALTH"]
    if obj_in.product_code not in allowed:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product code")
    policy = Policy(
        user_id=obj_in.user_id,
        product_code=obj_in.product_code,
        start_date=obj_in.start_date,
        end_date=obj_in.end_date,
    )
    db.add(policy)
    db.commit()
    db.refresh(policy)
    log_to_ledger("policy_created", {"policy_id": policy.id, "user_id": policy.user_id})
    return policy

def schedule_first_premium(db: Session, policy: Policy) -> Premium:
    amount = Decimal('100.00')
    premium = Premium(
        policy_id=policy.id,
        due_date=policy.start_date,
        amount=amount,
    )
    db.add(premium)
    db.commit()
    db.refresh(premium)
    log_to_ledger("premium_scheduled", {"premium_id": premium.id, "policy_id": policy.id})
    return premium

def deduct_premium(db: Session, premium: Premium) -> Premium:
    if premium.paid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Premium already paid")
    premium.paid = True
    db.add(premium)
    db.commit()
    db.refresh(premium)
    log_to_ledger("premium_deducted", {"premium_id": premium.id, "amount": str(premium.amount)})
    # Update policy status if needed (e.g., mark as EXPIRED elsewhere)
    return premium

def file_claim(db: Session, obj_in: ClaimCreate) -> Claim:
    policy = db.query(Policy).filter(Policy.id == obj_in.policy_id).first()
    if not policy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Policy not found")
    if policy.status != "ACTIVE":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Policy not active")
    api_key = os.getenv("INSURANCE_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    # Mock external request - we simply assume success
    try:
        requests.get("https://mock-insurance-provider/verify", headers=headers, timeout=2)
    except Exception:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="External verification failed")
    claim = Claim(
        policy_id=obj_in.policy_id,
        claim_date=datetime.utcnow(),
        amount_requested=obj_in.amount_requested,
    )
    db.add(claim)
    db.commit()
    db.refresh(claim)
    log_to_ledger("claim_filed", {"claim_id": claim.id, "amount_requested": str(claim.amount_requested)})
    return claim
