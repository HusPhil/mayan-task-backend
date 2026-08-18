from sqlalchemy.orm import Session

from app.core.database import SessionLocal, get_db
from app.core.dto import TaskCreate, TaskRead
from app.core.enums import TaskStatus
from app.models.task_model import Task

db = get_db()


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, new_task: TaskCreate) -> TaskRead:
        task = Task(title=new_task.title, description=new_task.description)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return TaskRead(
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=task.created_at,
        )
