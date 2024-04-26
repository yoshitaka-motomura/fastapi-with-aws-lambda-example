from typing import Optional, List
import strawberry
from database import get_db
from utils.libs import generate_ulid
import time


@strawberry.type
class Memo:
    id: str
    title: str
    description: str
    created_at: int
    updated_at: int

    def __init__(self, id: str, title: str, description: str, created_at: int, updated_at: int):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @strawberry.field
    def _id(self) -> str:
        return self.id


@strawberry.type
class MemoUpdateResponse:
    id: str
    title: str
    description: str
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

    def get_memos(self, limit: Optional[int] = 10) -> List[Memo]:
        ret = []
        for memo in self.collection.find({}).limit(limit):
            ret.append(Memo(id=memo['_id'], title=memo['title'], description=memo['description']))
        return ret

    def get_memo_by_id(self, id: str):
        memo = self.collection.find_one({'_id': id})
        if memo:
            return Memo(id=memo['_id'], title=memo['title'], description=memo['description'])
        return None

    def create_memo(self, title: str, description: str):
        now = int(time.time())
        memo = {
            '_id': generate_ulid(),
            'title': title,
            'description': description,
            'createdAt': now,
            'updatedAt': now,
        }
        self.collection.insert_one(memo)
        return Memo(
            id=memo['_id'],
            title=memo['title'],
            description=memo['description'],
            created_at=memo['createdAt'],
            updated_at=memo['updatedAt'])

    def update_memo(self, id: str, title: str, description: str):
        now = int(time.time())
        memo = {
            'title': title,
            'description': description,
            'updatedAt': now,
        }
        self.collection.update_one({'_id': id}, {'$set': memo})
        return MemoUpdateResponse(
            id=id,
            title=title,
            description=description,
            updated_at=now)
