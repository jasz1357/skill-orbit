from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class CategoryRecord(Base):
    __tablename__ = "categories"

    id: Mapped[str] = mapped_column(String(48), primary_key=True)
    label: Mapped[str] = mapped_column(String(32), nullable=False)
    label_cn: Mapped[str] = mapped_column(String(32), nullable=False, default="")
    color: Mapped[str] = mapped_column(String(7), nullable=False)
    radius: Mapped[float] = mapped_column(Float, nullable=False)
    tilt_x: Mapped[float] = mapped_column(Float, nullable=False)
    tilt_y: Mapped[float] = mapped_column(Float, nullable=False)
    tilt_z: Mapped[float] = mapped_column(Float, nullable=False)
    speed: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    skills: Mapped[list["SkillRecord"]] = relationship(back_populates="category")


class UserRecord(Base):
    __tablename__ = "users"
    __table_args__ = (
        Index("ix_users_username", "username", unique=True),
        Index("ix_users_email", "email", unique=True),
    )

    id: Mapped[str] = mapped_column(String(48), primary_key=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    skills: Mapped[list["SkillRecord"]] = relationship(back_populates="user")


class SkillRecord(Base):
    __tablename__ = "skills"
    __table_args__ = (
        Index("ix_skills_user_id", "user_id"),
        Index("ix_skills_category_id", "category_id"),
        Index("ix_skills_created_at", "created_at"),
    )

    id: Mapped[str] = mapped_column(String(48), primary_key=True)
    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False)
    note: Mapped[str] = mapped_column(Text, nullable=False, default="")
    source_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    angle: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)

    user: Mapped[Optional[UserRecord]] = relationship(back_populates="skills")
    category: Mapped[CategoryRecord] = relationship(back_populates="skills")
