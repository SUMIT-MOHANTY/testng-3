import pytest
from fastapi.testclient import TestClient
from backend.app import app
from backend.dependencies import get_db
from backend.models import Base
from backend.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use an in‑memory SQLite DB for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
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

def test_create_policy(client):
    # Create a dummy user via existing user endpoint or mock - here we assume user_id=1 exists
    payload = {
        "user_id": 1,
        "product_code": "HOME",
        "start_date": "2030-01-01T00:00:00Z",
        "end_date": "2035-01-01T00:00:00Z",
    }
    response = client.post("/api/v1/policies/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["product_code"] == "HOME"

def test_premium_deduction(client, db):
    # Assuming a policy with id=1 and a premium due now exists
    from backend.models.policy import Premium, Policy
    from datetime import datetime, timedelta
    policy = Policy(user_id=1, product_code="AUTO", status="ACTIVE", start_date=datetime.utcnow(), end_date=datetime.utcnow()+timedelta(days=365))
    db.add(policy)
    db.commit()
    db.refresh(policy)
    premium = Premium(policy_id=policy.id, due_date=datetime.utcnow()-timedelta(hours=1), amount=100.00)
    db.add(premium)
    db.commit()
    from backend.jobs.premium_scheduler import run_premium_scheduling
    run_premium_scheduling(db)
    db.refresh(premium)
    assert premium.paid is True
