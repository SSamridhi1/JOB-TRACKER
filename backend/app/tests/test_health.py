"""
Example backend test.

Why this file exists:
    Demonstrates the testing pattern for the project (pytest + FastAPI's
    TestClient) with the one endpoint that's actually implemented right
    now: /health. Future feature tests should follow this same shape.
"""


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
