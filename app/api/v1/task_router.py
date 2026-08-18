from fastapi import APIRouter

router = APIRouter(prefix="/tasks")


@router.get("/")
def root():
    return "Task router is working well!"
