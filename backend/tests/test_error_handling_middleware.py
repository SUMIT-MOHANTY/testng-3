from fastapi import HTTPException
from backend.app.core.error_handling import ErrorHandlingMiddleware
def test_error_handling(client, monkeypatch):
    # Monkey‑patch a route to raise an exception
    @client.app.get("/boom")
    def boom():
        raise RuntimeError("boom")
    response = client.get("/boom")
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal Server Error"
