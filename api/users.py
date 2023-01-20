from typing import Optional, List
from uuid import UUID, uuid4
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    email: str
    is_active: Optional[bool] = False
    bio: Optional[str]

@router.get('/')
async def root():
    return {'message':'Hello world'}

@router.get('/users', response_model=List[User])
async def get_users():
    return users

@router.post('/user', status_code=201)
async def create_user(user: User):
    users.append(user)
    return user

@router.get('/user/{id}')
async def get_user_by_id(id: int):
    return {"user":users[id]}