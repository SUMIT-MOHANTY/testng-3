from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ... import crud, schemas, dependencies, security

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.UserRead)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    if crud.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user_in)

@router.get("/me", response_model=schemas.UserRead)
def read_current_user(current_user: models.User = Depends(dependencies.get_current_user)):
    return current_user
