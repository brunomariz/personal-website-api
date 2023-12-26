from fastapi.testclient import TestClient
from app.main import app

test_client = TestClient(app)

def test_resources():
    response = test_client.get("/resources")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json().get("children") is not None
    assert response.json().get("id") is not None
    assert response.json().get("resources") is not None

def test_software_engineering_content():
    response = test_client.get("/resources")

    include_text ="- MAC321 - Laboratório de Programação Orientada a Objetos - IME/USP https://youtube.com/playlist?list=PLTeQ2u81sjqfsFNWrUCIoqJZBSJrai8M7" 
    print([item for item in response.json()["children"] if item["id"]=="computer-engineering"])
    computer_engineering = next((item for item in response.json()["children"] if item["id"] == "computer-engineering"), None)
    software_engineering = next((item for item in computer_engineering["resources"] if item["id"] == "software-engineering"), None)
    assert include_text in software_engineering["data"]

def test_resource_paths():
    response = test_client.get("/resources/paths")
    assert "/resources/computer-graphics" in response.json()
    assert "/resources/cool-networking-websites" in response.json()
    assert "/resources/information-security" in response.json()
    assert "/resources/software-engineering" in response.json()
    assert "/resources/historical-design-stuff" in response.json()

