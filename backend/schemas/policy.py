from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class PolicyCreate(BaseModel):
    user_id: int
    product_code: str
    start_date: datetime
    end_date: datetime

class PolicyRead(BaseModel):
    id: int
    user_id: int
    product_code: str
    status: str
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True

class PremiumRead(BaseModel):
    id: int
    policy_id: int
    due_date: datetime
    amount: Decimal
    paid: bool

    class Config:
        orm_mode = True

class ClaimCreate(BaseModel):
    policy_id: int
    amount_requested: Decimal

class ClaimRead(BaseModel):
    id: int
    policy_id: int
    claim_date: datetime
    amount_requested: Decimal
    approved: bool
    payout_amount: Decimal | None = None

    class Config:
        orm_mode = True
