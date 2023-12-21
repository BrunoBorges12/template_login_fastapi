from fastapi import APIRouter
from  api.routes import user

api_router = APIRouter()


api_router.include_router(user.api,prefix='/users',tags=['users'])
