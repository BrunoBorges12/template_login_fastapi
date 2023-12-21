from models.user import User
from  sqlmodel import Session
from models.user import User,UserCreate  # noqa: F811
from sqlmodel import select
from typing import Optional
class UserService():

    def get_by_email(self,db:Session,email:str) -> Optional[User]:
        query_user = select(User).where(User.email== email)
        results = db.exec(query_user).first()
        return results
    def create_user(self,db:Session,user_data:UserCreate)-> User:
        create_user_db = User(email=user_data.email,name=user_data.name,age=user_data.age)
        db.add(create_user_db) 
        db.commit()
        db.refresh(create_user_db)

        return create_user_db            



user = UserService()