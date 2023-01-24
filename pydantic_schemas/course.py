from typing import Optional
from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int
    
    
class CreateCourse(CourseBase):
    pass
    
# class for Data response
class Course(CourseBase):
    id: Optional[int]

    class Config:
        orm_mode = True