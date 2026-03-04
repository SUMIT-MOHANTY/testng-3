from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import crud
from backend.crud import policy as policy_crud
from backend.schemas.policy import PolicyCreate, PolicyRead
from backend.dependencies import get_db, get_current_active_user
router = APIRouter()

@router.post("/api/v1/policies/", response_model=PolicyRead, status_code=status.HTTP_201_CREATED)
def create_policy_endpoint(policy_in: PolicyCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    if policy_in.user_id != current_user.id and not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to create policy for another user")
    policy = policy_crud.create_policy(db, policy_in)
    policy_crud.schedule_first_premium(db, policy)
    return policy

@router.get("/api/v1/policies/{policy_id}", response_model=PolicyRead)
def get_policy(policy_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    policy = db.query(crud.models.policy.Policy).filter(crud.models.policy.Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Policy not found")
    if policy.user_id != current_user.id and not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return policy
