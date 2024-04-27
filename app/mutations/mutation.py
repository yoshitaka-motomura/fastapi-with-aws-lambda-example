import strawberry
from models.memo import Memo, MemoService, MemoUpdateResponse


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_memo(self, title: str, description: str) -> Memo:
        service = MemoService()
        return service.create_memo(title, description)

    @strawberry.mutation
    def update_memo(self, id: str, title: str, description: str) -> MemoUpdateResponse:
        service = MemoService()
        return service.update_memo(id, title, description)
