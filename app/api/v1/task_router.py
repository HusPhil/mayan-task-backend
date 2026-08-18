from uuid import UUID

from fastapi import APIRouter, Depends

from app.api.params import TaskSearchParams
from app.api.dependency_injection import get_task_service
from app.core.dto import TaskCreate, TaskRead, TaskUpdate
from app.core.errors import TaskNotFoundError
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks API v1"])


@router.post("/", response_model=TaskRead)
def create_task(
    new_task: TaskCreate, task_service: TaskService = Depends(get_task_service)
):
    created_task = task_service.create_task(new_task)
    return created_task


@router.get("/", response_model=list[TaskRead])
def get_all_tasks(
    task_service: TaskService = Depends(get_task_service),
    params: TaskSearchParams = Depends(),
):

    all_tasks = task_service.get_all_tasks(params)
    return all_tasks


@router.get("/{task_id}", response_model=TaskRead)
def get_task_by_id(
    task_id: UUID,
    task_service: TaskService = Depends(get_task_service),
):
    task = task_service.get_task_by_id(task_id)

    if not task:
        raise TaskNotFoundError(task_id)

    return task


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: UUID,
    task_update: TaskUpdate,
    task_service: TaskService = Depends(get_task_service),
):
    task = task_service.update_task(task_id, task_update)

    if not task:
        raise TaskNotFoundError(task_id)

    return task


@router.delete("/{task_id}", response_model=TaskRead)
def delete_task(task_id: UUID, task_service: TaskService = Depends(get_task_service)):
    task = task_service.delete_task(task_id)

    if not task:
        raise TaskNotFoundError(task_id)

    return task
