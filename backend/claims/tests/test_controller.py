def test_submit_claim_happy(client):
    resp = client.post(
        "/api/v1/claims",
        json={"policy_id": "11111111-1111-1111-1111-111111111111", "user_id": "22222222-2222-2222-2222-222222222222", "amount": 1000, "currency": "USD", "documents": ["doc1"]},
        headers={"X-Idempotency-Key": "key-123", "Authorization": "Bearer test"},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["status"] == "SUBMITTED"
