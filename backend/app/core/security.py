from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from typing import Any, Union
import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(payload: str):
    signed = jwt.encode(
        {"payload": payload, "exp": datetime.now() + timedelta(seconds=30)},
        "secret",
        algorithm=ALGORITHM,
    )
    return signed


def verific_password_hash(password: str, hash_password) -> str:
    return pwd_context.verify(password, hash_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
