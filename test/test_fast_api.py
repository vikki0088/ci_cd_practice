from fastapi.testclient import TestClient

from src.rest import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, CI/CD World!"}

def test_add_numbers():
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}