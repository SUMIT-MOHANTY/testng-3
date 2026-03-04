import pytest, asyncio
from httpx import AsyncClient
from backend.app import create_app
from backend.dependencies import get_db
from backend.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
async def client(db):
    async def override_get_db():
        try:
            yield db
        finally:
            pass
    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

async def test_user_crud_flow(client):
    # create user
    resp = await client.post("/api/v1/users/", json={"username":"alice","email":"alice@example.com","password":"secret"})
    assert resp.status_code == 200
    data = resp.json()
    user_id = data["id"]
    token = data["access_token"]
    # get user (self role simulated)
    resp = await client.get(f"/api/v1/users/{user_id}", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    # update user
    resp = await client.put(f"/api/v1/users/{user_id}", json={"username":"alice2"}, headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    # delete user (should fail without admin)
    resp = await client.delete(f"/api/v1/users/{user_id}", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 403

async def test_role_assignment_and_admin_actions(client, db):
    # create admin role and admin user directly via DB
    from backend.models.role import Role
    from backend.models import User
    admin_role = Role(name="admin")
    db.add(admin_role)
    admin_user = User(username="admin", email="admin@example.com", password_hash="hash")
    admin_user.roles.append(admin_role)
    db.add(admin_user)
    db.commit()
    # simulate token for admin (mocked, no real verification)
    admin_token = "admin-token"
    # assign role to alice
    resp = await client.post(f"/api/v1/users/{user_id}/roles", json={"role_names":["admin"]}, headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
    # admin deletes alice
    resp = await client.delete(f"/api/v1/users/{user_id}", headers={"Authorization": f"Bearer {admin_token}"})
    assert resp.status_code == 200
