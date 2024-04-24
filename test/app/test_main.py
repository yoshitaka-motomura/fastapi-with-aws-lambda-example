from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "About"}


def test_contact():
    response = client.get("/contact")
    assert response.status_code == 200
    assert response.json() == {"message": "Contact"}