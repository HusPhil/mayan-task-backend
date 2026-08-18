from fastapi import APIRouter, Body, Depends, Response, status

from app.core.dependency_injection import get_task_service
from app.core.dto import TaskCreate, TaskRead
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks")


@router.get("/")
def get_all_tasks():
    return "Task router is working well!"


@router.post("/", response_model=TaskRead)
def create_task(
    new_task: TaskCreate, task_service: TaskService = Depends(get_task_service)
):
    created_task = task_service.create_task(new_task)
    return created_task
