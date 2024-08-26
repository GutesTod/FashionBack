from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.advertisements import advertisement_router
from src.categories import category_router
from src.services import service_router

from src.base import db_manager

from src.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.init(settings.POSTGRES_URL)
    yield
    await db_manager.close()

app = FastAPI(lifespan=lifespan)

app.include_router(advertisement_router)
app.include_router(category_router)
app.include_router(service_router)

print(settings.POSTGRES_URL)