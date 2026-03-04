from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field, validator

class ClaimCreateDTO(BaseModel):
    policy_id: str
    user_id: str
    amount: Decimal = Field(..., gt=0)
    currency: str = "USD"
    documents: List[str]

    @validator("currency")
    def _len(cls, v):
        if len(v) != 3:
            raise ValueError("currency must be 3‑letter ISO")
        return v

class ClaimValidateDTO(BaseModel):
    documents: List[str]

class ClaimApproveDTO(BaseModel):
    approver_id: str

class ClaimPayoutDTO(BaseModel):
    pass

class ClaimResponseDTO(BaseModel):
    claim_id: str
    status: str
    created_at: str

class ErrorDTO(BaseModel):
    detail: str
