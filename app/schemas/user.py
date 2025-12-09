from sqlmodel import SQLModel,Field
from typing import Optional

class UserBase(SQLModel):
    username:str = Field(...,min_length=3,max_length=50)
    email:str = Field(...,min_length=5,max_length=100)
    age:int=Field(...,ge=1,le=120)
    bio:Optional[str]=None
class UserCreate(UserBase):
    password:str=Field(..., min_length=6, max_length=72)
class UserRead(UserBase):
    id:int
class UserUpdate(SQLModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[str] = Field(None, min_length=5, max_length=100)
    age: Optional[int] = Field(None, ge=1, le=120)
    bio: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6, max_length=72)
 