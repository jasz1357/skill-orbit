from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.db.ai_library_seed import AI_LIBRARY_ITEMS
from app.db.models import AILibraryItemRecord
from app.models.ai_library import AILibraryItemCreate, AILibraryItemRead, AILibraryItemUpdate
from app.repositories.ai_skills import _search_terms


def ensure_ai_library_seed(db: Session) -> None:
    existing_ids = set(db.scalars(select(AILibraryItemRecord.id)).all())
    existing_signatures = {
        (
            record.item_type,
            record.title,
            record.tools_json,
            record.steps_json,
            record.outputs_json,
        )
        for record in db.scalars(select(AILibraryItemRecord)).all()
    }
    now = datetime.now(timezone.utc)
    for item in AI_LIBRARY_ITEMS:
        signature = (
            item["item_type"],
            item["title"],
            json.dumps(item.get("tools", []), ensure_ascii=False),
            json.dumps(item.get("steps", []), ensure_ascii=False),
            json.dumps(item.get("outputs", []), ensure_ascii=False),
        )
        if item["id"] in existing_ids or signature in existing_signatures:
            continue
        db.add(_create_record(item, now))
        existing_ids.add(item["id"])
        existing_signatures.add(signature)
    db.commit()


def list_ai_library_items(
    db: Session,
    item_type: Optional[str] = None,
    query: Optional[str] = None,
    category_id: Optional[str] = None,
    active: bool = True,
    limit: int = 500,
) -> list[AILibraryItemRead]:
    stmt = select(AILibraryItemRecord)
    if active:
        stmt = stmt.where(AILibraryItemRecord.is_active.is_(True))
    if item_type:
        stmt = stmt.where(AILibraryItemRecord.item_type == item_type)
    if category_id:
        stmt = stmt.where(AILibraryItemRecord.category_id == category_id)
    if query:
        clauses = []
        searchable_columns = (
            AILibraryItemRecord.title,
            AILibraryItemRecord.category_label,
            AILibraryItemRecord.summary,
            AILibraryItemRecord.tools_json,
            AILibraryItemRecord.steps_json,
            AILibraryItemRecord.outputs_json,
            AILibraryItemRecord.tags_json,
        )
        for term in _search_terms(query):
            pattern = f"%{term}%"
            compact_pattern = f"%{term.replace(' ', '')}%"
            for column in searchable_columns:
                clauses.append(column.ilike(pattern))
                clauses.append(func.replace(func.lower(column), " ", "").like(compact_pattern.lower()))
        if clauses:
            stmt = stmt.where(or_(*clauses))
    stmt = stmt.order_by(AILibraryItemRecord.item_type, AILibraryItemRecord.importance.desc(), AILibraryItemRecord.title).limit(limit)
    return [_to_read(record) for record in db.scalars(stmt).all()]


def get_ai_library_item(db: Session, item_id: str) -> Optional[AILibraryItemRead]:
    record = db.get(AILibraryItemRecord, item_id)
    return _to_read(record) if record else None


def create_ai_library_item(db: Session, payload: AILibraryItemCreate) -> AILibraryItemRead:
    data = payload.model_dump()
    item_id = data.pop("id") or _slugify(data["title"])
    if db.get(AILibraryItemRecord, item_id):
        item_id = f"{item_id[:86]}-{uuid4().hex[:8]}"
    now = datetime.now(timezone.utc)
    record = _create_record({"id": item_id, **data}, now)
    db.add(record)
    db.commit()
    db.refresh(record)
    return _to_read(record)


def update_ai_library_item(db: Session, item_id: str, payload: AILibraryItemUpdate) -> Optional[AILibraryItemRead]:
    record = db.get(AILibraryItemRecord, item_id)
    if not record:
        return None
    data = payload.model_dump(exclude_unset=True)
    for key, value in data.items():
        if key in {"tools", "steps", "outputs", "tags"}:
            setattr(record, f"{key}_json", json.dumps(value or [], ensure_ascii=False))
        else:
            setattr(record, key, value)
    record.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(record)
    return _to_read(record)


def delete_ai_library_item(db: Session, item_id: str) -> bool:
    record = db.get(AILibraryItemRecord, item_id)
    if not record:
        return False
    record.is_active = False
    record.updated_at = datetime.now(timezone.utc)
    db.commit()
    return True


def _create_record(data: dict, now: datetime) -> AILibraryItemRecord:
    return AILibraryItemRecord(
        id=data["id"],
        item_type=data["item_type"],
        title=data["title"],
        category_id=data.get("category_id", ""),
        category_label=data.get("category_label", ""),
        summary=data.get("summary", ""),
        tools_json=json.dumps(data.get("tools", []), ensure_ascii=False),
        steps_json=json.dumps(data.get("steps", []), ensure_ascii=False),
        outputs_json=json.dumps(data.get("outputs", []), ensure_ascii=False),
        tags_json=json.dumps(data.get("tags", []), ensure_ascii=False),
        source_section=data.get("source_section", ""),
        importance=data.get("importance", 50),
        is_active=data.get("is_active", True),
        created_at=now,
        updated_at=now,
    )


def _to_read(record: AILibraryItemRecord) -> AILibraryItemRead:
    return AILibraryItemRead(
        id=record.id,
        item_type=record.item_type,
        title=record.title,
        category_id=record.category_id,
        category_label=record.category_label,
        summary=record.summary,
        tools=_loads(record.tools_json),
        steps=_loads(record.steps_json),
        outputs=_loads(record.outputs_json),
        tags=_loads(record.tags_json),
        source_section=record.source_section,
        importance=record.importance,
        is_active=record.is_active,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


def _loads(raw: str) -> list[str]:
    try:
        value = json.loads(raw or "[]")
        return value if isinstance(value, list) else []
    except json.JSONDecodeError:
        return []


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug or f"ai-library-{uuid4().hex[:8]}")[:100]
