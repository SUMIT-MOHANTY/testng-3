import pytest
from fastapi.testclient import TestClient
from backend.main import app  # assumes main FastAPI app is defined here
from backend.auth.dependencies import get_current_user
from backend.users.models import User

client = TestClient(app)

class MockUser:
    def __init__(self, id, role):
        self.id = id
        self.role = role

@pytest.fixture(autouse=True)
def override_auth(monkeypatch):
    def mock_user():
        return MockUser(id=1, role='insurer')
    monkeypatch.setattr('backend.auth.dependencies.get_current_user', mock_user)

def test_create_and_retrieve_policy():
    # create policy
    resp = client.post('/insurance/policies/', json={"user_id":1,"product_code":"PROD123","start_date":"2024-01-01"})
    assert resp.status_code == 201
    policy = resp.json()
    pid = policy['id']
    # retrieve
    resp2 = client.get(f'/insurance/policies/{pid}')
    assert resp2.status_code == 200
    data = resp2.json()
    assert data['id'] == pid

def test_claim_filing(monkeypatch):
    # use same user (owner)
    # first create policy
    resp = client.post('/insurance/policies/', json={"user_id":1,"product_code":"PROD123","start_date":"2024-01-01"})
    pid = resp.json()['id']
    # file claim
    claim_resp = client.post('/insurance/claims/', json={"policy_id": pid, "claim_amount_cents": 5000})
    assert claim_resp.status_code == 201
    claim = claim_resp.json()
    assert claim['policy_id'] == pid
