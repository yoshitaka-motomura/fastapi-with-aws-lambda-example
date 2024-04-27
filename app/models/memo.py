import time
from typing import Optional, List
import strawberry
from database import get_db
from utils.libs import generate_ulid


@strawberry.type
class Memo:
    id: str
    title: str
    description: str
    created_at: int
    updated_at: int

    @strawberry.field
    def _id(self) -> str:
        return self.id


@strawberry.type
class MemoUpdateResponse:
    result: bool
    id: str
    updated_at: int

    @strawberry.field
    def _id(self) -> str:
        return self.id


class MemoService:
    db = None
    collection = None

    def __init__(self):
        self.db = get_db()
        self.collection = self.db['memos']

    @staticmethod
    def _data_to_memo(data):
        return Memo(
            id=data['_id'],
            title=data['title'],
            description=data['description'],
            created_at=data['created_at'],
            updated_at=data['updated_at'])

    def get_memos(self, limit: Optional[int] = 10) -> List[Memo]:
        ret = []
        for memo in self.collection.find({}).limit(limit):
            ret.append(self._data_to_memo(memo))
        return ret

    def get_memo_by_id(self, id: str):
        memo = self.collection.find_one({'_id': id})
        if memo:
            return self._data_to_memo(memo)
        return None

    def create_memo(self, title: str, description: str):
        now = int(time.time())
        memo = {
            '_id': generate_ulid(),
            'title': title,
            'description': description,
            'created_at': now,
            'updated_at': now,
        }
        self.collection.insert_one(memo)
        return Memo(
            id=memo['_id'],
            title=memo['title'],
            description=memo['description'],
            created_at=memo['created_at'],
            updated_at=memo['updated_at'])

    def update_memo(self, id: str, title: str, description: str):
        memo = {
            'title': title,
            'description': description,
            'updated_at': int(time.time()),
        }
        result = self.collection.update_one({'_id': id}, {'$set': memo})

        if result.modified_count == 0:
            return MemoUpdateResponse(result=False, id=id, updated_at=None)

        return MemoUpdateResponse(
            result=True,
            id=id,
            updated_at=memo['updated_at'])
