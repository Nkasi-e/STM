from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select 

from db.models.user import User
from db.models.course import Course
from pydantic_schemas.user_schema import UserCreate

# Get user by ID - Controller
async def get_user_by_id(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one()

# Get user by email - Controller
def get_user_by_email(db: Session, email: str):
    query = db.query(User).filter(User.email == email).first()
    return query

# GEtting all the users in the db - Controller
async def get_users(db: AsyncSession):
    query = select(User).order_by(User.id)
    result = await db.execute(query)
    return result.scalars().all()

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