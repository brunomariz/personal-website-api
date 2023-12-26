from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_file():
    response = test_client.get("/file")
    assert response.json() == {"message": "file"}

def test_cv_pt():
    response = test_client.get("/file/cv?lang=pt-BR")
    assert response.status_code == 200
    assert int(response.headers["content-length"]) > 30000

def test_cv_en():
    response = test_client.get("/file/cv?lang=en-US")
    assert response.status_code == 200
    assert int(response.headers["content-length"]) > 30000
