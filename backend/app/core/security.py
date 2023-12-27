from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(payload: str):
    pass


def verific_password_hash(password: str, hash_password) -> str:
    pwd_context.verify(password, hash_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
