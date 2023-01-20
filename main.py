from typing import Optional, List
from uuid import UUID, uuid4
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title = "Common Books",
    description = "API for reading and writing books",
    version = "0.1.0",
    terms_of_service = "API url service",
    contact = {
        "name":"Nkasi Emmanuel",
        "email":"emmanuelnkasi@gmail.com",
        "url":"http://github.com/nkasi-e"
    },
    license_info = {
        "name":"MIT"
    },
)

users = []

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    email: str
    is_active: Optional[bool] = False
    bio: Optional[str]

@app.get('/')
async def root():
    return {'message':'Hello world'}

@app.get('/users', response_model=List[User])
async def get_users():
    return users

@app.post('/user', status_code=201)
async def create_user(user: User):
    users.append(user)
    return user

@app.get('/user/{id}')
async def get_user_by_id(id: int = Path(..., description = "The ID if user you want retrieve", gt=0), q: str = Query(None, max_length=5)):
    return {"user":users[id], "query": q}