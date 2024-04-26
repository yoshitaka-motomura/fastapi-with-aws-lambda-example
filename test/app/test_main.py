from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from models import Memo
client = TestClient(app)


def test_graphql_get_memo():
    mocked_memos = [
        Memo(id="1", title="title1", description="description1"),
        Memo(id="2", title="title2", description="description2")
    ]

    with patch("schema.get_memo") as mock_get_memo:
        mock_get_memo.return_value = mocked_memos

        response = client.post(
            "/graphql",
            json={"query": "{ memos { id title description } }"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "data": {
                "memos": [
                    {"id": "1", "title": "title1", "description": "description1"},
                    {"id": "2", "title": "title2", "description": "description2"}
                ]
            }
        }

        mock_get_memo.assert_called_once()


def test_graphql_memo_not_found():
    with patch("schema.get_memo_by_id") as mock_get_memo_by_id:
        mock_get_memo_by_id.return_value = None

        response = client.post(
            "/graphql",
            json={"query": "{ memo(id: \"3\") { id title description } }"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "data": {
                "memo": None
            }
        }

        mock_get_memo_by_id.assert_called_once_with("3")