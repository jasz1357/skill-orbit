from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import CategoryRecord, SkillRecord
from app.models.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.models.skill import SkillCreate, SkillRead, SkillUpdate


def list_categories(db: Session) -> list[CategoryRead]:
    records = db.scalars(select(CategoryRecord).order_by(CategoryRecord.created_at)).all()
    return [_category_to_read(record) for record in records]


def get_category(db: Session, category_id: str) -> Optional[CategoryRead]:
    record = db.get(CategoryRecord, category_id)
    return _category_to_read(record) if record else None


def create_category(db: Session, payload: CategoryCreate) -> Optional[CategoryRead]:
    category_id = payload.id or f"cat_{uuid4().hex[:10]}"
    if db.get(CategoryRecord, category_id):
        return None

    tilt_x, tilt_y, tilt_z = payload.tilt
    record = CategoryRecord(
        id=category_id,
        label=payload.label,
        label_cn=payload.label_cn,
        color=payload.color,
        radius=payload.radius,
        tilt_x=tilt_x,
        tilt_y=tilt_y,
        tilt_z=tilt_z,
        speed=payload.speed,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return _category_to_read(record)


def update_category(db: Session, category_id: str, payload: CategoryUpdate) -> Optional[CategoryRead]:
    record = db.get(CategoryRecord, category_id)
    if not record:
        return None

    data = payload.model_dump(exclude_unset=True)
    if "tilt" in data:
        record.tilt_x, record.tilt_y, record.tilt_z = data.pop("tilt")
    for key, value in data.items():
        setattr(record, key, value)

    record.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(record)
    return _category_to_read(record)


def delete_category(db: Session, category_id: str) -> bool:
    record = db.get(CategoryRecord, category_id)
    if not record:
        return False

    fallback = db.scalar(select(CategoryRecord).where(CategoryRecord.id != category_id).order_by(CategoryRecord.created_at))
    if not fallback:
        return False

    for skill in db.scalars(select(SkillRecord).where(SkillRecord.category_id == category_id)):
        skill.category_id = fallback.id
        skill.updated_at = datetime.now(timezone.utc)

    db.delete(record)
    db.commit()
    return True


def list_skills(db: Session, user_id: str, query: Optional[str] = None, category_id: Optional[str] = None) -> list[SkillRead]:
    stmt = select(SkillRecord).where(SkillRecord.user_id == user_id)
    if category_id:
        stmt = stmt.where(SkillRecord.category_id == category_id)
    if query:
        pattern = f"%{query}%"
        stmt = stmt.where(SkillRecord.name.ilike(pattern) | SkillRecord.note.ilike(pattern))
    records = db.scalars(stmt.order_by(SkillRecord.created_at.desc())).all()
    return [_skill_to_read(record) for record in records]


def get_skill(db: Session, skill_id: str, user_id: str) -> Optional[SkillRead]:
    record = db.scalar(select(SkillRecord).where(SkillRecord.id == skill_id, SkillRecord.user_id == user_id))
    return _skill_to_read(record) if record else None


def create_skill(db: Session, payload: SkillCreate, user_id: str) -> SkillRead:
    record = SkillRecord(id=f"sk_{uuid4().hex[:12]}", user_id=user_id, **payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return _skill_to_read(record)


def update_skill(db: Session, skill_id: str, payload: SkillUpdate, user_id: str) -> Optional[SkillRead]:
    record = db.scalar(select(SkillRecord).where(SkillRecord.id == skill_id, SkillRecord.user_id == user_id))
    if not record:
        return None

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, key, value)
    record.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(record)
    return _skill_to_read(record)


def delete_skill(db: Session, skill_id: str, user_id: str) -> bool:
    record = db.scalar(select(SkillRecord).where(SkillRecord.id == skill_id, SkillRecord.user_id == user_id))
    if not record:
        return False
    db.delete(record)
    db.commit()
    return True


def _category_to_read(record: CategoryRecord) -> CategoryRead:
    return CategoryRead(
        id=record.id,
        label=record.label,
        label_cn=record.label_cn,
        color=record.color,
        radius=record.radius,
        tilt=(record.tilt_x, record.tilt_y, record.tilt_z),
        speed=record.speed,
    )


def _skill_to_read(record: SkillRecord) -> SkillRead:
    return SkillRead(
        id=record.id,
        name=record.name,
        category_id=record.category_id,
        note=record.note,
        source_text=record.source_text,
        angle=record.angle,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )
