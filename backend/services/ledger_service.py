from typing import List, Dict

class LedgerService:
    def __init__(self):
        self._store: List[Dict] = []

    def write_entry(self, entry: Dict) -> Dict:
        """Append an entry to the in‑memory ledger and return it."""
        self._store.append(entry)
        return entry

    def list_entries(self) -> List[Dict]:
        return list(self._store)

ledger_service = LedgerService()
