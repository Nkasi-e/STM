from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    role: int

# class for Data response
class User(UserCreate):
    id: Optional[int]
    created_at: datetime
    updated_at: datetime
    
class Config:
    orm_mode = True
    '''
    this is very important if using an orm in conjunction with pydantic... allows pydantic to work with orm if used and set to True 
    
    '''