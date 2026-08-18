from uuid import UUID

from fastapi import HTTPException, status


class TaskNotFoundError(HTTPException):
    def __init__(self, task_id: UUID):
        self.task_id = task_id
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID: '{task_id}' not found",
        )
