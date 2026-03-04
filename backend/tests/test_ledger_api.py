import unittest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

class TestLedgerAPI(unittest.TestCase):
    def test_create_and_list(self):
        payload = {'data': {'msg': 'hello'}}
        resp = client.post('/api/v1/ledger/', json=payload)
        self.assertEqual(resp.status_code, 201)
        self.assertDictContainsSubset(payload, resp.json())

        list_resp = client.get('/api/v1/ledger/')
        self.assertEqual(list_resp.status_code, 200)
        self.assertTrue(any(item['data'] == payload['data'] for item in list_resp.json()))

if __name__ == '__main__':
    unittest.main()
