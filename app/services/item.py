import asyncio
import time
from uuid import uuid4
from db import DB
from app.schemas.item import Item
from fastapi import BackgroundTasks
from app.services.task import TaskService

class ItemService:
    """
    Simple service class for managing items.
    """

    @classmethod
    async def create_item(cls, item: Item):
        item_id = str(uuid4())
        DB[item_id] = {"item": item.dict(), "created_at": time.time()}
        return item_id
    
    @classmethod
    async def get_items(cls):
        return {item_id: data["item"] for item_id, data in DB.items()}
    
    @classmethod
    async def get_item(cls, item_id: str):
        if item_id in DB:
            return DB[item_id]["item"]
        return {"message": "Item not found"}
    
    @classmethod
    async def delete_item(cls, item_id: str, background_tasks: BackgroundTasks):
        task_id = TaskService.create_and_run_task(
            background_tasks,
            cls._delete_item_after_delay,
            item_id,
            20
        )
        return {"message": f"Scheduled deletion for item {item_id}", "task_id": task_id}
    
    @classmethod
    async def _delete_item_after_delay(cls, item_id: str, delay: int):
        await asyncio.sleep(delay)
        if item_id in DB:
            del DB[item_id]
