def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_config(client):
    r = client.get("/config")
    assert r.status_code == 200
    data = r.json()
    assert "app_name" in data and "key_vault_url" in data
