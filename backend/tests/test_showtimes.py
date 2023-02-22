import pytest
from fastapi.testclient import TestClient
from main import app

def test_get_showtimes_by_movie(client):
    response = client.get("/showtimes/?movie_name=Inception")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_showtimes_by_city(client):
    response = client.get("/showtimes/?city=Boston")
    assert response.status_code == 200
    assert len(response.json()) > 0
