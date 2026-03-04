from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies import get_db, require_role
from ... import crud, schemas, models

router = APIRouter()

@router.post("/users", response_model=schemas.UserRead, dependencies=[require_role("Admin")])
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user_in.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = crud.create_user(db, user_in)
    return user

@router.get("/users/me", response_model=schemas.UserRead)
def read_current_user(current_user: models.User = Depends(require_role("User", "Bank", "Insurer", "Admin"))):
    return current_user
