from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ... import crud, schemas, dependencies

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)
