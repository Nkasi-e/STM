import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Sequence
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp



class Role(enum.Enum):
    admin = "admin"
    student = "student"
    
    
class User(Timestamp, Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    profile = relationship("Profile", back_populates="owner", uselist=False)
    
class Profile(Timestamp, Base):
    __tablename__ = 'profile'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # setting foreign key
    owner = relationship("User", back_populates="profile") # setting relationship
