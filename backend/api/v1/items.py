from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ... import crud, schemas, dependencies

router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_items(db, skip=skip, limit=limit)

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db), current_user: dict = Depends(dependencies.get_current_user)):
    return crud.create_item(db, item, user_id=current_user.get("sub", 0))
