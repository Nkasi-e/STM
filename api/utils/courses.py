from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course import CreateCourse

# Get course by ID - Controller
def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

# GEtting all the courses in the db - Controller
def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

# Create course Controller
def create_course(db: Session, course: CreateCourse):
    db_course = Course(
        title = course.title,
        description = course.description,
        user_id = course.user_id # passed manually because there is no authentication
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course