import strawberry
from fastapi import FastAPI
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter
import queries.query
import mutations.mutation

app = FastAPI()

schema = strawberry.Schema(query=queries.query.Query, mutation=mutations.mutation.Mutation)

graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")

app.include_router(graphql_app, prefix="/graphql")
handler = Mangum(app)
