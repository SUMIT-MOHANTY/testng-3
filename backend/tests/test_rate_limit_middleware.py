def test_rate_limit(client):
    # Perform max_requests + 1 calls quickly; expect 429 on the last
    for i in range(6):
        resp = client.get("/health")
        if i < 5:
            assert resp.status_code == 200
        else:
            assert resp.status_code == 429
