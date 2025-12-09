from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.core.jwt import verify_token
from app.db.database import get_session
from app.db.crud import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
def current_user(
        token:str = Depends(oauth2_scheme),
        session:Session=Depends(get_session)
):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate":"Bearer"}
        )
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user(session,user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user