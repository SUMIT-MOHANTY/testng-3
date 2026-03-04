import unittest
from backend.services.ledger_service import ledger_service

class TestLedgerService(unittest.TestCase):
    def setUp(self):
        # reset in‑memory store before each test
        ledger_service._store.clear()

    def test_write_and_list(self):
        entry = {'data': {'key': 'value'}}
        ledger_service.write_entry(entry)
        self.assertEqual(len(ledger_service.list_entries()), 1)
        self.assertDictEqual(ledger_service.list_entries()[0], entry)

if __name__ == '__main__':
    unittest.main()
