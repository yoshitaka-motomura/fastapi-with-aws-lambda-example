from typing import Optional, List
import strawberry
from models.memo import Memo, MemoService


@strawberry.type
class Query:
    @strawberry.field
    def memos(self, limit: Optional[int] = 10) -> List[Memo]:
        service = MemoService()
        return service.get_memos(limit)

    @strawberry.field
    def get_memo(self, id: str) -> Optional[Memo]:
        service = MemoService()
        return service.get_memo_by_id(id)
