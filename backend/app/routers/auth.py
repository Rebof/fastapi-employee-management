# app/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.hashing import Hash
from app.auth.token import create_access_token
from app.crud.admin import get_admin_by_email
from app.schemas.admin import TokenResponse
from app.database import get_db

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = get_admin_by_email(db, request.username)
    if not admin or not Hash.verify(request.password, admin.password): # type: ignore
        raise HTTPException(status_code=403, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": admin.email})
    return {"access_token": access_token, "token_type": "bearer"}
