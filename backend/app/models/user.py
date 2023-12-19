from sqlmodel import SQLModel,Field
from typing import Optional


class UserBase(SQLModel):
    name:str
    email:str
    age:str 


class User(UserBase,table=True):
    id:Optional[int] =  Field(default=None,primary_key=True)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    pass