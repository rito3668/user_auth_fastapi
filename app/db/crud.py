from sqlmodel import Session,select

from app.db.models import User
from app.schemas.user import UserUpdate
def create_user(session:Session,user:User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(session:Session,user_id:int):
    statement = select(User).where(User.id==user_id)
    result = session.exec(statement).first()
    return result

def list_users(session:Session,limit:int=10,offset:int=0):
    statement = select(User).offset(offset).limit(limit)
    results = session.exec(statement).all()
    return results

def update_user(session:Session,user_id:int,data:dict):
    statement = select(User).where(User.id==user_id)
    user = session.exec(statement).first()
    if not user:
        return None
    for key,value in data.items():
        setattr(user,key,value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session:Session,user_id:int):
    statement = select(User).where(User.id==user_id)
    user = session.exec(statement).first()
    if not user:
        return None
    session.delete(user)
    session.commit()
    return True
