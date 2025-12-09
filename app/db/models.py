from sqlmodel import SQLModel,Field

from typing import Optional

class User(SQLModel,table=True):
    id:Optional[int]=Field(None,primary_key=True)
    username:str
    email:str
    age:int
    bio:Optional[str]=None
    password:str