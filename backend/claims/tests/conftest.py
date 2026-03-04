import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.claims import claims_router

@pytest.fixture(scope="session")
def app():
    app = FastAPI()
    app.include_router(claims_router, prefix="/api/v1")
    return app

@pytest.fixture
def client(app):
    return TestClient(app)
