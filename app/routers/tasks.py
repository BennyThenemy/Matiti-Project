from fastapi import APIRouter
from app.services.task import TaskService

router = APIRouter()

@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    return await TaskService.get_task_status(task_id)