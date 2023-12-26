from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_health_check():
    response = test_client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "Bruno Mariz Personal Website API"}

def test_root():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello!!!"}