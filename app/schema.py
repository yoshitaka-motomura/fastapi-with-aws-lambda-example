import typing
import strawberry
from .models import Memo

# Query resolvers for the GraphQL API.


def get_memo() -> object:
    return [
        Memo(id=1, title="Memo 1", description="Description 1"),
        Memo(id=2, title="Memo 2", description="Description 2"),
    ]


def get_memo_by_id(id: int):
    return Memo(id=id, title=f"Memo {id}", description=f"Description {id}")


@strawberry.type
class Query:
    memos: typing.List[Memo] = strawberry.field(resolver=get_memo)
    memo: Memo = strawberry.field(resolver=get_memo_by_id)
