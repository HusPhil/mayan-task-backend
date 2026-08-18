from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, field_validator
from app.core.enums import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskRead(BaseModel):
    id: UUID
    title: str
    description: str
    status: TaskStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
