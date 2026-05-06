from __future__ import annotations

from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import verify_access_token
from app.db.models import UserRecord
from app.db.session import get_db
from app.repositories import users

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> UserRecord:
    if not credentials:
        raise HTTPException(status_code=401, detail="Missing access token")
    user_id = verify_access_token(credentials.credentials)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired access token")
    user = users.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


__all__ = ["get_current_user", "get_db"]
