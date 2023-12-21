from api.deps import SessionDepends
from fastapi import APIRouter,HTTPException
from  service.user import user as user_service
from models.user import UserCreate
api = APIRouter()

@api.get('/user')
def create_user(db:SessionDepends,user_data:UserCreate):
    user = user_service.get_by_email(db,user_data.email)
    if user:
        raise  HTTPException(status_code=400, detail="email já existe")
    user_create = user_service.create_user(db,user_data)
    return user_create
     