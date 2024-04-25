import os
import strawberry
from fastapi import FastAPI
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter
from schema import Query


app = FastAPI()

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")

app.include_router(graphql_app, prefix="/graphql")
handler = Mangum(app)
