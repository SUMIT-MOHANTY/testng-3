from backend.audit.ledger_client import LedgerClient

def record_event(claim_id: str, event: str, payload: dict):
    client = LedgerClient()
    client.record(claim_id, event, payload)
