from api.deps import SessionDepends
from fastapi import APIRouter
from  service.user import user
api = APIRouter()

@api.get('/user')
def create_user(db:SessionDepends):
     return user.get_by_email(db,'brunosb02@hotmail.com')