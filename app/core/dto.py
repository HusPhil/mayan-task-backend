from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.enums import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskRead(BaseModel):
    title: str
    description: str
    status: TaskStatus
    created_at: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
