from api.deps import SessionDepends
from fastapi import APIRouter

api = APIRouter()

@api.get('/user')
def create_user(db:SessionDepends):
    return 'agora foi'