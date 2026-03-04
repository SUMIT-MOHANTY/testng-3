from pydantic import BaseModel, Field

class LedgerEntry(BaseModel):
    data: dict = Field(..., description='Arbitrary JSON payload for the ledger')
