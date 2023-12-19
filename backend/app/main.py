from fastapi import FastAPI,Depends
from typing import Annotated

from core.config import settings
from sqlmodel import Session
from models.user  import SQLModel,UserRead,UserCreate,User
from db.engine import engine,get_session

SQLModel.metadata.create_all(engine)

app = FastAPI(title=settings.PROJECT_NAME)

