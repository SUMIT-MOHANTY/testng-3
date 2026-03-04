from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, security, dependencies

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/register', response_model=schemas.UserRead)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    existing = crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db, user_in)

@router.post('/login')
def login(user_in: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    user = crud.get_user_by_email(db, user_in.email)
    if not user or not security.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    access_token = security.create_access_token({'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
