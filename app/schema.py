import typing
import strawberry
from models import Memo
from database import get_db


# Query resolvers for the GraphQL API.

def get_memo(limit: typing.Optional[int] = 10) -> typing.List[Memo]:
    db = get_db()
    collection = db['memos']
    ret = []
    for memo in collection.find({}).limit(limit):
        ret.append(Memo(id=memo['_id'], title=memo['title'], description=memo['description']))
    return ret


def get_memo_by_id(id: str):
    db = get_db()
    collection = db['memos']
    memo = collection.find_one({'_id': id})
    if memo:
        return Memo(id=memo['_id'], title=memo['title'], description=memo['description'])
    else:
        return None


# Query type for the GraphQL API.
@strawberry.type
class Query:
    @strawberry.field
    def memos(self, limit: typing.Optional[int] = 10) -> typing.List[Memo]:
        return get_memo(limit)

    @strawberry.field
    def memo(self, id: str) -> typing.Optional[Memo]:
        return get_memo_by_id(id)
