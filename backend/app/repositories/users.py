from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.db.models import SkillRecord, UserRecord
from app.models.auth import UserCreate, UserRead


def create_user(db: Session, payload: UserCreate, is_admin: bool = False) -> Optional[UserRead]:
    existing = db.scalar(
        select(UserRecord).where((UserRecord.username == payload.username) | (UserRecord.email == payload.email))
    )
    if existing:
        return None

    record = UserRecord(
        id=f"usr_{uuid4().hex[:12]}",
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
        is_admin=is_admin,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return to_read(record)


def authenticate_user(db: Session, username_or_email: str, password: str) -> Optional[UserRecord]:
    record = db.scalar(
        select(UserRecord).where((UserRecord.username == username_or_email) | (UserRecord.email == username_or_email))
    )
    if not record or not verify_password(password, record.password_hash):
        return None
    return record


def get_user(db: Session, user_id: str) -> Optional[UserRecord]:
    return db.get(UserRecord, user_id)


def to_read(record: UserRecord) -> UserRead:
    return UserRead(id=record.id, username=record.username, email=record.email, is_admin=record.is_admin)


def ensure_admin_user(db: Session, username: str, email: str, password: str) -> UserRecord:
    admin = db.scalar(select(UserRecord).where(UserRecord.username == username))
    if not admin:
        admin = UserRecord(
            id=f"usr_{uuid4().hex[:12]}",
            username=username,
            email=email,
            password_hash=hash_password(password),
            is_admin=True,
        )
        db.add(admin)
        db.flush()

    db.query(SkillRecord).filter(SkillRecord.user_id.is_(None)).update(
        {"user_id": admin.id, "updated_at": datetime.now(timezone.utc)}
    )
    db.commit()
    db.refresh(admin)
    return admin
