from fastapi import APIRouter,HTTPException,Depends
from sqlmodel import Session,select
from app.core.deps import current_user
from app.schemas.user import UserRead
from app.db.database import get_session
from app.db.models import User
from app.core.security import verify_password
from app.core.jwt import create_access_token

router = APIRouter()

@router.post("/login")
def login(email:str,password:str,session:Session=Depends(get_session)):
    statement = select(User).where(User.email==email)
    user = session.exec(statement).first()
    if not user:
        raise HTTPException(status_code=400,detail="Invalid email or password")
    
    if not verify_password(password,user.password):
        raise HTTPException(status_code=400,detail="Invalid email or password")
    
    token = create_access_token({"sub":str(user.id)})
    return {
        "access_token":token,
        "token_type":"bearer"
    }

@router.get("/me",response_model=UserRead)
def get_me(user=Depends(current_user)):
    return user