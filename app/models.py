import strawberry


@strawberry.type
class Memo:
    id: int
    title: str
    description: str
