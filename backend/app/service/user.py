from models.user import User
from  sqlmodel import Session
from models.user import User  # noqa: F811
from sqlmodel import select
from typing import Optional
class UserService():

    def get_by_email(self,db:Session,email:str) -> Optional[User]:
        query_user = select(User).where(User.email== email)
        results = db.exec(query_user)
        return results
        



user = UserService()