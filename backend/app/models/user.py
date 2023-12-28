from sqlmodel import SQLModel, Field, AutoString
from pydantic import EmailStr
from typing import Optional


class UserBase(SQLModel):
    name: str
    email: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    password: str


class User(UserBase, table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    pass


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
