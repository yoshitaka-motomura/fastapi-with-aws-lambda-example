from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_graphql():
    response = client.post(
        "/graphql",
        json={"query": "{ memos { id title description } }"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "memos": [
                {"id": 1, "title": "Memo 1", "description": "Description 1"},
                {"id": 2, "title": "Memo 2", "description": "Description 2"},
            ]
        }
    }


def test_graphql_memo():
    response = client.post(
        "/graphql",
        json={"query": "{ memo(id: 1) { id title description } }"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "memo": {"id": 1, "title": "Memo 1", "description": "Description 1"}
        }
    }
