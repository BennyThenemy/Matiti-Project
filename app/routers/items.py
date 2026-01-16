from fastapi import APIRouter, BackgroundTasks
from app.schemas.item import Item
from app.services.item import ItemService


router = APIRouter()

@router.post("/items/")
async def create_item(item: Item):
    item_id = await ItemService.create_item(item)
    return {"message": "Item created", "item_id": item_id}

@router.get("/items/{item_id}")
async def get_item(item_id: str):
    return await ItemService.get_item(item_id)

@router.get("/items")
async def get_all_items():
    return await ItemService.get_items()

@router.delete("/items/{item_id}")
async def delete_item(item_id: str, background_tasks: BackgroundTasks):
    return await ItemService.delete_item(item_id, background_tasks)
