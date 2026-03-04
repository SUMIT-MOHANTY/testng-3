from pydantic import BaseModel, EmailStr
from typing import List, Optional
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

class AccountRead(BaseModel):
    id: int
    balance: float

    class Config:
        orm_mode = True
