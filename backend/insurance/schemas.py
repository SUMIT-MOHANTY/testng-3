from pydantic import BaseModel
from datetime import date, datetime

class PolicyCreate(BaseModel):
    user_id: int
    product_code: str
    start_date: date

class PolicyResponse(BaseModel):
    id: int
    user_id: int
    product_code: str
    status: str
    start_date: date
    end_date: date | None = None
    created_at: datetime
    first_premium_due: date | None = None

    class Config:
        orm_mode = True

class ClaimCreate(BaseModel):
    policy_id: int
    claim_amount_cents: int

class ClaimResponse(BaseModel):
    id: int
    policy_id: int
    claim_amount_cents: int
    status: str
    submitted_at: datetime
    resolved_at: datetime | None = None

    class Config:
        orm_mode = True

class PremiumScheduleResponse(BaseModel):
    policy_id: int
    next_due_date: date
    amount_cents: int

    class Config:
        orm_mode = True
