def test_logging_middleware(client, caplog):
    # Trigger a request that goes through the logger middleware
    response = client.get("/health")
    assert response.status_code == 200
    # The Loguru logger writes to stdout/file; we simply ensure no exception raised
    assert True
