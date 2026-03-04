from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ... import crud, schemas, dependencies

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=List[schemas.ItemRead])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.ItemRead)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    return crud.create_item(db, item_in, user_id=current_user.id)
