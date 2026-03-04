from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .schemas.role import RoleRead

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    roles: List[RoleRead] = []
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Placeholder for Item schemas
