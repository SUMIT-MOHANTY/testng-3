from pydantic import BaseModel, condecimal, PositiveInt

class TransferRequest(BaseModel):
    recipient_id: PositiveInt
    amount: condecimal(gt=0, max_digits=12, decimal_places=2)

class TransferResponse(BaseModel):
    success: bool
    new_balance: condecimal(max_digits=12, decimal_places=2) | None = None
    detail: str | None = None
