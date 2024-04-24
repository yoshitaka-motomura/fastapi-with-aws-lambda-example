import typing
import strawberry
from fastapi import FastAPI
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter

"""
This is a simple example of a GraphQL API using Strawberry and FastAPI.
If you use AWS, it might be better to choose AppSync
"""
app = FastAPI()


# @app.middleware("http")
# async def add_cors_header(request, call_next):
#     print("request")
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     return response


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

"""
playground disable argument is `graphql_ide=None`
"""
graphql_app = GraphQLRouter(schema, graphql_ide=None)

app.include_router(graphql_app, prefix="/graphql")
handler = Mangum(app)
