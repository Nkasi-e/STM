from sqlalchemy.orm import Session

from db.models.user import User
from db.models.course import Course
from pydantic_schemas.user_schema import UserCreate

# Get user by ID - Controller
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get user by email - Controller
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# GEtting all the users in the db - Controller
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Create User Controller
def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Getting all courses that belongs to a specific user
def get_user_courses(user_id: int, db: Session ):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses