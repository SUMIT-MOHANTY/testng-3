from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas.policy import ClaimCreate, ClaimRead
from backend.dependencies import get_db, get_current_active_user
from backend.crud.policy import file_claim
router = APIRouter()

@router.post("/api/v1/claims/", response_model=ClaimRead, status_code=status.HTTP_201_CREATED)
def file_claim_endpoint(claim_in: ClaimCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    # Ensure the user owns the policy they are claiming against
    policy = db.query(crud.models.policy.Policy).filter(crud.models.policy.Policy.id == claim_in.policy_id).first()
    if not policy:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Policy not found")
    if policy.user_id != current_user.id and not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to file claim for this policy")
    claim = file_claim(db, claim_in)
    return claim
