from fastapi import APIRouter,HTTPException,Depends
from sqlmodel import Session
from app.core.security import hash_password
from app.db.database import get_session
from app.db.models import User
from app.schemas.user import UserCreate,UserRead,UserUpdate
from app.core.deps import current_user
from app.core.deps import current_user
from app.db.crud import (
    create_user,
    get_user,list_users,update_user,delete_user
)

router = APIRouter()

@router.post("/",response_model=UserRead,status_code=201)
def create_user_route(user:UserCreate,session:Session = Depends(get_session)):
    print("DEBUG >>> RAW PASSWORD =", user.password, type(user.password))
    hashed_pw = hash_password(user.password)
    new_user = User(
        username=user.username,
        email = user.email,
        age = user.age,
        bio = user.bio,
        password=hashed_pw
    )
    return create_user(session,new_user)

@router.get("/{user_id}",response_model=UserRead)
def get_user_route(user_id:int,session:Session=Depends(get_session)):
    user = get_user(session,user_id)
    if not user:
        raise HTTPException(status_code=404,detail=f"User with {user_id} userid Not Found!")
    return user

@router.get("/",response_model=list[UserRead])
def list_users_route(limit:int=10,offset:int=0,session:Session=Depends(get_session)):
    return list_users(session,limit,offset)

@router.put("/{user_id}",response_model=UserRead)
def update_user_route(user_id:int,user_data:UserUpdate,session:Session=Depends(get_session),current_user = Depends(current_user)):
   if user_id!= current_user.id:
       raise HTTPException(
           status_code=403,
           detail="You cant modify this user!"
       )

   update_dict = user_data.dict(exclude_unset=True)
   if "password" in update_dict:
       update_dict["password"] = hash_password(update_dict["password"])
   updated_user = update_user(session,user_id,update_dict)
   if not updated_user:
       raise HTTPException(status_code=404,detail="User not found")
   return updated_user

@router.delete("/{user_id}",status_code=204)
def delete_user_route(user_id:int,session:Session=Depends(get_session),current_user = Depends(current_user)):
    if user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You cannot delete another user's account"
        )
    deleted = delete_user(session,user_id)
    if not deleted:
        raise HTTPException(status_code=404,detail=f"User with {user_id} userid cant be deleted!")
    return None


