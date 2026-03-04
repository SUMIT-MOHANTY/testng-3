from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    items: List[ItemRead] = []
    class Config:
        orm_mode = True
