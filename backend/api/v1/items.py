from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.get("/items", response_model=list[schemas.ItemRead])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_items(db, skip, limit)

@router.post("/items", response_model=schemas.ItemRead)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db), current_user = Depends(dependencies.get_current_user)):
    return crud.create_item(db, item, current_user.id)
