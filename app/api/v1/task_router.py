from typing import Annotated
from uuid import UUID

from anyio import Path
from fastapi import APIRouter, Body, Depends, Response, status

from app.core.dependency_injection import get_task_service
from app.core.dto import TaskCreate, TaskRead
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks")


@router.get("/", response_model=list[TaskRead])
def get_all_tasks(task_service: TaskService = Depends(get_task_service)):
    all_tasks = task_service.get_all_tasks()
    return all_tasks


@router.post("/", response_model=TaskRead)
def create_task(
    new_task: TaskCreate, task_service: TaskService = Depends(get_task_service)
):
    created_task = task_service.create_task(new_task)
    return created_task


@router.get("/{task_id}", response_model=TaskRead)
def get_task_by_id(
    task_id: str,
    task_service: TaskService = Depends(get_task_service),
):
    task = task_service.get_task_by_id(task_id)

    if not task:
        return status.HTTP_404_NOT_FOUND

    return task
