from fastapi import FastAPI

from core.config import settings
from models.user  import SQLModel
from db.engine import engine
from  api.config_api import api_router
SQLModel.metadata.create_all(engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router,prefix="/api/v1")