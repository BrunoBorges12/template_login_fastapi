from api.deps import SessionDepends
from fastapi import APIRouter, HTTPException
from service.user import user as user_service
from models.user import UserCreate, UserRead

api = APIRouter()


@api.post("/signUp")
def create_user(db: SessionDepends, user_data: UserCreate):
    user = user_service.get_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="email já existe")
    user_create = user_service.create_user(db, user_data)
    return user_create


@api.post("/signIn")
def login(db: SessionDepends, user_data: UserRead):
    user = user_service.user_authentication(
        db, email=user_data.email, password=user_data.password
    )
    print(user)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou passoword errado ")
    return user
