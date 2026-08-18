from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.database import get_db
from app.core.dto import TaskCreate, TaskRead
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

    def get_all_tasks(self) -> list[TaskRead]:
        statement = select(Task)

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
