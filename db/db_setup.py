from sqlalchemy import create_engine # synchronous engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession # async engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

 # Synchronous connection with psycopg2
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:070399@localhost/coursedb"

# async connection with asyncpg
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:070399@localhost/coursedb"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)

# asycn engine
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

# asynchronously
Async_SessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# async dependency
async def async_get_db():
    async with Async_SessionLocal() as db:
        yield db
        await db.commit()