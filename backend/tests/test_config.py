def test_config(client):
    response = client.get("/config")
    assert response.status_code == 200
    json = response.json()
    assert "LOG_ENDPOINT" in json
    assert json["LOG_ENDPOINT"] == "https://mock-logging.local"
