import pytest
from fastapi.testclient import TestClient
from main import app

def test_user_login(client):
    # Mock login credentials
    response = client.post(
        "/users/login",
        data={"email": "john@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful!"
    assert response.json()["user_id"] == 1
