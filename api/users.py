from typing import Optional, List

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import fastapi

from db.db_setup import get_db
from api.utils.users import *
from pydantic_schemas.user_schema import *



router = fastapi.APIRouter()


@router.get('/')
async def root():
    return {'message':'Hello world'}

# Get all users route
@router.get('/users', status_code=200)
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return {"All User": users}

@router.post('/user', status_code=201)
async def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user is not None:
        raise HTTPException(
            status_code=409,
            detail = f'user with email {user.email} already exists'
        )
    new_user = create_user(db, user)
    return {"data": new_user}

@router.get('/user/{user_id}')
async def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code = 404,
            detail = f'user with id {user_id} does not exist'
        )
    return user

# get all courses belonging to a specific user
@router.get('/user/{user_id}/courses')
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id, db)
    if courses == []:
        raise HTTPException(
            status_code=404,
            detail = f'User with id {user_id} course catalogue is empty. Please register a new course'
        )
    return courses