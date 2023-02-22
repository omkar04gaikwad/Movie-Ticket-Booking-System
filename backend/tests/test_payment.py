import pytest
from fastapi.testclient import TestClient
from main import app

def test_process_payment(client):
    # Mock processing a payment
    headers = {"Authorization": "Bearer 1"}
    response = client.post(
        "/payments/",
        headers=headers,
        data={"booking_id": 1, "amount": 200}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Payment successful!"
