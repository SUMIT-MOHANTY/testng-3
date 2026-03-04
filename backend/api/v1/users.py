from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. ..dependencies import get_db, get_current_user, require_role
from ... import crud, schemas
from ...security import create_access_token

router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post("/", response_model=schemas.UserRead)
def create_user_endpoint(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.user.create_user(db, user_in)
    token = create_access_token({"sub": user.username})
    # Return token in a header‑like field for simplicity
    return {**user.__dict__, "access_token": token}

@router.get("/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db), current=Depends(require_role("admin", "self"))):
    user = crud.user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, user_in: schemas.UserUpdate, db: Session = Depends(get_db), current=Depends(require_role("admin", "self"))):
    user = crud.user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.user.update_user(db, user, user_in)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current=Depends(require_role("admin"))):
    user = crud.user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.user.delete_user(db, user)
    return {"detail": "deleted"}

@router.post("/{user_id}/roles")
def assign_roles(user_id: int, payload: dict, db: Session = Depends(get_db), current=Depends(require_role("admin"))):
    role_names = payload.get("role_names", [])
    user = crud.user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for name in role_names:
        role = crud.user.get_role_by_name(db, name)
        if not role:
            raise HTTPException(status_code=404, detail=f"Role {name} not found")
        crud.user.add_role_to_user(db, user, role)
    return {"detail": "roles assigned"}
