from typing import Annotated
from fastapi import Query
from app.api.enums import SortDirection
from app.core.enums import TaskStatus


from typing import Annotated
from fastapi import Query
from app.api.enums import SortDirection
from app.core.enums import TaskStatus


class TaskSearchParams:
    def __init__(
        self,
        q: str | None = None,
        s: Annotated[list[TaskStatus] | None, Query()] = None,
        sort: SortDirection = SortDirection.DESCENDING,
    ):
        self.query = q
        self.status = s
        self.sort = sort
