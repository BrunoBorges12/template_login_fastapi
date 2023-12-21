from sqlmodel import Session
from db.engine import engine
from typing import Annotated
from fastapi import Depends
def get_db():
    with Session(engine) as session:
        yield session


SessionDepends = Annotated[Session,Depends(get_db)]
