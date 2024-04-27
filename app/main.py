import strawberry
from fastapi import FastAPI
from mangum import Mangum
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
import queries.query
import mutations.mutation

app = FastAPI()

schema = strawberry.Schema(query=queries.query.Query,
                           mutation=mutations.mutation.Mutation,
                           config=StrawberryConfig(auto_camel_case=True))

graphql_app = GraphQLRouter(schema, graphql_ide="graphiql")

app.include_router(graphql_app, prefix="/graphql")
handler = Mangum(app)
