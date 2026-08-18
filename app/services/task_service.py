from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.api.params import TaskSearchParams
from app.api.enums import SortDirection
from app.core.dto import TaskCreate, TaskRead, TaskUpdate
from app.models.task_model import Task


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, new_task: TaskCreate) -> TaskRead:
        task = Task(title=new_task.title, description=new_task.description)

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return TaskRead(
            id=task.id,
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=task.created_at,
        )

    def get_all_tasks(self, params: TaskSearchParams) -> list[TaskRead]:
        statement = select(Task)

        if params.query:
            statement = statement.where(Task.title.ilike(f"%{params.query}%"))

        if params.status:
            statement = statement.where(Task.status.in_(params.status))

        sort_column = getattr(Task, "created_at")

        if params.sort == SortDirection.DESCENDING:
            statement = statement.order_by(sort_column.desc())
        elif params.sort == SortDirection.ASCENDING:
            statement = statement.order_by(sort_column.asc())

        tasks = self.db.scalars(statement).all()

        return [
            TaskRead(
                id=task.id,
                title=task.title,
                description=task.description,
                status=task.status,
                created_at=task.created_at,
            )
            for task in tasks
        ]

    def get_task_by_id(self, task_id: UUID) -> TaskRead | None:
        task = self.db.get(Task, task_id)

        if not task:
            return None

        return TaskRead.model_validate(task)

    def update_task(self, task_id: str, task_update: TaskUpdate) -> TaskRead | None:

        task = self.db.get(Task, task_id)

        if not task:
            return None

        if task_update.title != None:
            task.title = task_update.title

        if task_update.description != None:
            task.description = task_update.description

        if task_update.status != None:
            task.status = task_update.status

        self.db.commit()
        self.db.refresh(task)

        return TaskRead.model_validate(task)

    def delete_task(self, task_id: str) -> TaskRead | None:
        task = self.db.get(Task, task_id)

        if not task:
            return None

        self.db.delete(task)
        self.db.commit()

        return TaskRead.model_validate(task)
