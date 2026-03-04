from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter(prefix='/items', tags=['items'])

@router.get('/', response_model=list[schemas.ItemRead])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_items(db, skip, limit)

@router.post('/', response_model=schemas.ItemRead)
def create_item(item_in: schemas.ItemCreate, current_user = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    return crud.create_item(db, item_in, current_user.id)
