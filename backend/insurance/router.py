from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.auth.dependencies import get_current_user, require_role
from . import crud, schemas, utils, constants
from datetime import date
import logging

logger = logging.getLogger('insurance')
insurance_router = APIRouter(prefix="/insurance", tags=["insurance"])

@insurance_router.post('/policies/', response_model=schemas.PolicyResponse, status_code=status.HTTP_201_CREATED)
def create_policy_endpoint(payload: schemas.PolicyCreate, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    require_role(current_user, 'insurer')
    if not utils.validate_product_code(payload.product_code):
        raise HTTPException(status_code=400, detail='Invalid product code')
    policy = crud.create_policy(db, payload)
    premium = crud.schedule_first_premium(db, policy)
    resp = schemas.PolicyResponse.from_orm(policy)
    resp.first_premium_due = premium.due_date
    return resp

@insurance_router.get('/policies/{policy_id}', response_model=schemas.PolicyResponse)
def get_policy_endpoint(policy_id: int, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    policy = crud.get_policy(db, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail='Policy not found')
    if policy.user_id != current_user.id and not current_user.role == 'insurer':
        raise HTTPException(status_code=403, detail='Forbidden')
    resp = schemas.PolicyResponse.from_orm(policy)
    premium = crud.get_upcoming_premium(db, policy_id)
    resp.first_premium_due = premium.due_date if premium else None
    return resp

@insurance_router.post('/claims/', response_model=schemas.ClaimResponse, status_code=status.HTTP_201_CREATED)
def file_claim_endpoint(payload: schemas.ClaimCreate, current_user=Depends(get_current_user), db: Session = Depends(SessionLocal)):
    policy = crud.get_policy(db, payload.policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail='Policy not found')
    if policy.user_id != current_user.id:
        raise HTTPException(status_code=403, detail='Cannot claim on others policy')
    claim = crud.record_claim(db, payload)
    return schemas.ClaimResponse.from_orm(claim)
