# app/auth/oauth2.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.auth.token import verify_token
from app.models.admin import Admin
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email = verify_token(token, credentials_exception)
    admin = db.query(Admin).filter(Admin.email == email).first()
    if not admin:
        raise credentials_exception
    return admin
