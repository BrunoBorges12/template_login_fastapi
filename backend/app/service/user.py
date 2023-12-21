from app.models.user import User
from  sqlmodel import Session
class UserService():

    def get_by_email(self,db:Session,email:str) -> User:
        session = db
        email2= email
        return session,email2
        



user = UserService()