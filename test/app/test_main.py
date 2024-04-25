from fastapi.testclient import TestClient
from unittest.mock import patch
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


def test_graphql_memo_not_found():
    """Test that a memo that does not exist returns None"""
    with patch("app.schema.get_memo_by_id") as mock_get_memo_by_id:
        mock_get_memo_by_id.return_value = None

        response = client.post(
            "/graphql",
            json={"query": "{ memo(id: 3) { id title description } }"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "data": {
                "memo": None
            }
        }

        mock_get_memo_by_id.assert_called_once_with(3)