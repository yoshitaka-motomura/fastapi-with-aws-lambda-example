import typing
import strawberry
from fastapi import FastAPI
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Memo:
    id: int
    title: str
    description: str


def get_memo():
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


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
handler = Mangum(app)
