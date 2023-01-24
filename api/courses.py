import fastapi

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from db.db_setup import get_db
from api.utils.courses import *
from pydantic_schemas.course import *

router = fastapi.APIRouter()



@router.get('/courses', status_code=200)
async def read_courses(db : Session = Depends(get_db), skip: int = 0, limit: int = 100):
    courses = get_courses(db, skip, limit)
    return {"courses": courses }


@router.post('/courses', status_code=201)
async def create_new_course(course: CreateCourse, db: Session = Depends(get_db)):
    new_course = create_course(db, course)
    return new_course


@router.get('/courses/{course_id}')
async def read_course(course_id : int, db: Session = Depends(get_db) ):
    course = get_course_by_id(db, course_id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail =f'Course with id {course_id} not found'
        )
    return course



@router.patch('/courses/course_id}')
async def update_course():
    return {"courses": []}


@router.delete('/courses/{course_id}')
async def delete_course():
    return {"courses": []}


@router.get('/courses/{id}/sections')
async def read_course_section():
    return {"courses": []}