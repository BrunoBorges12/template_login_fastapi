from api.deps import SessionDepends
from fastapi import APIRouter, HTTPException
from service.user import user as user_service
from models.user import UserCreate, UserRead, Token
from core.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, FastAPI
from typing import Annotated


api = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login/access-token")


@api.post("/create-user")
def create_user(db: SessionDepends, user_data: UserCreate):
    user = user_service.get_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="email já existe")
    user_create = user_service.create_user(db, user_data)
    return user_create


@api.post("/login/access-token")
def login(
    db: SessionDepends, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = user_service.user_authentication(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Email ou passoword errado ")

    return Token(access_token=create_access_token(user.id))


@api.post("/item")
def item(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"usuarios": [{"token": token}, {"name": "bruno"}, {"name": "joão"}]}
