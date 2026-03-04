from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .. import dependencies, security
import httpx

router = APIRouter()

class LedgerEntry(BaseModel):
    data: dict

@router.post("/ledger/entries")
def write_ledger(entry: LedgerEntry, current_user = Depends(dependencies.get_current_user)):
    """Placeholder implementation that forwards the payload to the mock ledger.
    Replace with Azure Confidential Ledger SDK when available.
    """
    headers = {"Authorization": f"Bearer {security.settings.LEDGER_KEY}"}
    try:
        resp = httpx.post(security.settings.LEDGER_ENDPOINT, json=entry.dict(), headers=headers, timeout=5.0)
        resp.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return {"status": "submitted", "ledgerResponse": resp.json()}
