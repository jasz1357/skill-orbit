from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.core.security import create_access_token
from app.models.auth import TokenResponse, UserCreate, UserLogin, UserRead
from app.repositories import users

router = APIRouter()


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: UserCreate, db: Session = Depends(get_db)) -> TokenResponse:
    user = users.create_user(db, payload)
    if not user:
        raise HTTPException(status_code=409, detail="Username or email already exists")
    return TokenResponse(access_token=create_access_token(user.id), user=user)


@router.post("/login", response_model=TokenResponse)
async def login(payload: UserLogin, db: Session = Depends(get_db)) -> TokenResponse:
    user_record = users.authenticate_user(db, payload.username, payload.password)
    if not user_record:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return TokenResponse(access_token=create_access_token(user_record.id), user=users.to_read(user_record))


@router.get("/me", response_model=UserRead)
async def me(current_user=Depends(get_current_user)) -> UserRead:
    return users.to_read(current_user)
