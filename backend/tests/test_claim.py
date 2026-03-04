import pytest
from fastapi.testclient import TestClient
from backend.app import app
from backend.dependencies import get_db
from backend.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

def test_file_claim(client, db, monkeypatch):
    # Mock external insurance provider response
    def mock_get(*args, **kwargs):
        class Resp:
            status_code = 200
        return Resp()
    monkeypatch.setattr('requests.get', mock_get)
    from backend.models.policy import Policy, Claim
    from datetime import datetime, timedelta
    policy = Policy(user_id=1, product_code="HEALTH", status="ACTIVE", start_date=datetime.utcnow(), end_date=datetime.utcnow()+timedelta(days=365))
    db.add(policy)
    db.commit()
    db.refresh(policy)
    payload = {"policy_id": policy.id, "amount_requested": 500.00}
    response = client.post("/api/v1/claims/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["policy_id"] == policy.id
    assert data["approved"] is False  # not approved automatically in mock
