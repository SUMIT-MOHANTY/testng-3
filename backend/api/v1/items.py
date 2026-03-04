from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ... import crud, schemas, dependencies

router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_items(db, skip, limit)

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db),
               current_user: schemas.User = Depends(...)):
    # Placeholder for auth; assumes user_id = 1
    return crud.create_user_item(db, item, user_id=1)
