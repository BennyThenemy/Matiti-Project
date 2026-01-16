from fastapi import FastAPI
from app.routers import items_router, tasks_router

app = FastAPI(title="Benny's Application", description="An example for fastapi's BackgroundTasks",version="Matiti-v.1.0.0")

app.include_router(tags=["items"], prefix="/items", router=items_router)
app.include_router(tags=["tasks"], prefix="/tasks", router=tasks_router)

app.CORS_ALLOW_ORIGINS = ["*"]
app.CORS_ALLOW_CREDENTIALS = True
app.CORS_ALLOW_METHODS = ["*"]
app.CORS_ALLOW_HEADERS = ["*"]

