from uuid import uuid4
from typing import Callable, Any, Awaitable
from fastapi import BackgroundTasks

class TaskService:
    """
    A service class for managing background tasks.
    """
    tasks = {}

    @classmethod
    async def _run_and_update_status(cls, task_id: str, func: Callable[..., Awaitable[Any]], *args: Any):
        await func(*args)
        cls.tasks[task_id] = "completed"

    @classmethod
    def create_and_run_task(cls, background_tasks: BackgroundTasks, func: Callable[..., Awaitable[Any]], *args: Any):
        task_id = str(uuid4())
        cls.tasks[task_id] = "running"
        background_tasks.add_task(cls._run_and_update_status, task_id, func, *args)
        return task_id
    
    @classmethod
    async def get_task_status(cls, task_id: str):
        """
        Returns the status of a background task.
        """
        status = cls.tasks.get(task_id)
        if status is None:
            return {"status": "not_found"}
        return {"status": status}
