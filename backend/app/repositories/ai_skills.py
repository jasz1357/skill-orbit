from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.db.ai_skill_seed import AI_SKILLS
from app.db.ai_subskill_taxonomy import classify_subskill
from app.db.models import AISkillRecord
from app.models.ai_skill import AISkillCreate, AISkillRead, AISkillUpdate


def ensure_ai_skill_seed(db: Session) -> None:
    records_by_id = {record.id: record for record in db.scalars(select(AISkillRecord)).all()}
    seed_ids: set[str] = set()
    now = datetime.now(timezone.utc)
    for item in AI_SKILLS:
        item = _with_subskill(item)
        seed_ids.add(item["id"])
        record = records_by_id.get(item["id"])
        if record:
            _update_record(record, item, now)
        else:
            db.add(_create_record(item, now))

    for record_id, record in records_by_id.items():
        if record_id not in seed_ids:
            db.delete(record)
    db.commit()


def list_ai_skills(
    db: Session,
    query: Optional[str] = None,
    category_id: Optional[str] = None,
    core: Optional[bool] = None,
    active: bool = True,
    limit: int = 500,
) -> list[AISkillRead]:
    stmt = select(AISkillRecord)
    if active:
        stmt = stmt.where(AISkillRecord.is_active.is_(True))
    if category_id:
        stmt = stmt.where(AISkillRecord.category_id == category_id)
    if core is not None:
        stmt = stmt.where(AISkillRecord.is_core.is_(core))
    if query:
        clauses = []
        searchable_columns = (
            AISkillRecord.name,
            AISkillRecord.tool,
            AISkillRecord.category_label,
            AISkillRecord.description,
            AISkillRecord.tags_json,
            AISkillRecord.examples_json,
        )
        for term in _search_terms(query):
            pattern = f"%{term}%"
            compact_pattern = f"%{term.replace(' ', '')}%"
            for column in searchable_columns:
                clauses.append(column.ilike(pattern))
                clauses.append(func.replace(func.lower(column), " ", "").like(compact_pattern.lower()))
        if clauses:
            stmt = stmt.where(or_(*clauses))
    stmt = stmt.order_by(AISkillRecord.category_id, AISkillRecord.is_core.desc(), AISkillRecord.importance.desc(), AISkillRecord.name).limit(limit)
    return [_to_read(record) for record in db.scalars(stmt).all()]


def get_ai_skill(db: Session, skill_id: str) -> Optional[AISkillRead]:
    record = db.get(AISkillRecord, skill_id)
    return _to_read(record) if record else None


def create_ai_skill(db: Session, payload: AISkillCreate) -> AISkillRead:
    data = payload.model_dump()
    skill_id = data.pop("id") or _slugify(data["name"])
    if db.get(AISkillRecord, skill_id):
        skill_id = f"{skill_id[:58]}-{uuid4().hex[:8]}"
    now = datetime.now(timezone.utc)
    record = _create_record({"id": skill_id, **data}, now)
    db.add(record)
    db.commit()
    db.refresh(record)
    return _to_read(record)


def update_ai_skill(db: Session, skill_id: str, payload: AISkillUpdate) -> Optional[AISkillRead]:
    record = db.get(AISkillRecord, skill_id)
    if not record:
        return None
    data = payload.model_dump(exclude_unset=True)
    for key, value in data.items():
        if key in {"tags", "examples", "input_types", "output_types"}:
            setattr(record, f"{key}_json", json.dumps(value or [], ensure_ascii=False))
        else:
            setattr(record, key, value)
    record.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(record)
    return _to_read(record)


def delete_ai_skill(db: Session, skill_id: str) -> bool:
    record = db.get(AISkillRecord, skill_id)
    if not record:
        return False
    record.is_active = False
    record.updated_at = datetime.now(timezone.utc)
    db.commit()
    return True


def _create_record(data: dict, now: datetime) -> AISkillRecord:
    data = _with_subskill(data)
    return AISkillRecord(
        id=data["id"],
        name=data["name"],
        category_id=data["category_id"],
        category_label=data["category_label"],
        sub_skill_id=data.get("sub_skill_id", ""),
        sub_skill_label=data.get("sub_skill_label", ""),
        tool=data.get("tool", ""),
        stage=data.get("stage", ""),
        description=data.get("description", ""),
        tags_json=json.dumps(data.get("tags", []), ensure_ascii=False),
        examples_json=json.dumps(data.get("examples", []), ensure_ascii=False),
        input_types_json=json.dumps(data.get("input_types", []), ensure_ascii=False),
        output_types_json=json.dumps(data.get("output_types", []), ensure_ascii=False),
        difficulty=data.get("difficulty", 2),
        importance=data.get("importance", 50),
        is_core=data.get("is_core", False),
        is_active=data.get("is_active", True),
        created_at=now,
        updated_at=now,
    )


def _update_record(record: AISkillRecord, data: dict, now: datetime) -> None:
    data = _with_subskill(data)
    record.name = data["name"]
    record.category_id = data["category_id"]
    record.category_label = data["category_label"]
    record.sub_skill_id = data.get("sub_skill_id", "")
    record.sub_skill_label = data.get("sub_skill_label", "")
    record.tool = data.get("tool", "")
    record.stage = data.get("stage", "")
    record.description = data.get("description", "")
    record.tags_json = json.dumps(data.get("tags", []), ensure_ascii=False)
    record.examples_json = json.dumps(data.get("examples", []), ensure_ascii=False)
    record.input_types_json = json.dumps(data.get("input_types", []), ensure_ascii=False)
    record.output_types_json = json.dumps(data.get("output_types", []), ensure_ascii=False)
    record.difficulty = data.get("difficulty", 2)
    record.importance = data.get("importance", 50)
    record.is_core = data.get("is_core", False)
    record.is_active = data.get("is_active", True)
    record.updated_at = now


def _with_subskill(data: dict) -> dict:
    sub_skill_id, sub_skill_label = classify_subskill(data)
    return {**data, "sub_skill_id": sub_skill_id, "sub_skill_label": sub_skill_label}


def _to_read(record: AISkillRecord) -> AISkillRead:
    return AISkillRead(
        id=record.id,
        name=record.name,
        category_id=record.category_id,
        category_label=record.category_label,
        sub_skill_id=record.sub_skill_id,
        sub_skill_label=record.sub_skill_label,
        tool=record.tool,
        stage=record.stage,
        description=record.description,
        tags=_loads(record.tags_json),
        examples=_loads(record.examples_json),
        input_types=_loads(record.input_types_json),
        output_types=_loads(record.output_types_json),
        difficulty=record.difficulty,
        importance=record.importance,
        is_core=record.is_core,
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


def _search_terms(query: str) -> list[str]:
    raw = query.strip()
    if not raw:
        return []

    lower = raw.lower()
    terms: list[str] = [raw, raw.replace(" ", "")]
    terms.extend(part for part in re.split(r"[\s,，。.!?？/]+", raw) if len(part) >= 2)

    keyword_map = {
        "ppt": ["ppt", "slides", "deck", "演示", "幻灯"],
        "slide": ["ppt", "slides", "deck"],
        "presentation": ["ppt", "slides", "deck"],
        "代码": ["code", "coding", "cursor", "claude code", "编程"],
        "编程": ["code", "coding", "cursor", "claude code"],
        "code": ["code", "coding", "cursor", "claude code"],
        "图片": ["image", "visual", "design", "midjourney", "图像"],
        "图像": ["image", "visual", "design", "midjourney"],
        "设计": ["design", "visual", "canva", "排版"],
        "视频": ["video", "runway", "veo", "kling", "剪辑"],
        "音乐": ["audio", "music", "suno", "udio"],
        "声音": ["audio", "voice", "elevenlabs"],
        "研究": ["research", "search", "perplexity", "notebooklm"],
        "搜索": ["search", "research", "perplexity"],
        "论文": ["research", "paper", "elicit", "consensus"],
        "自动化": ["agent", "workflow", "automation", "n8n"],
        "流程": ["workflow", "automation", "agent"],
        "客服": ["customer", "support", "intercom", "zendesk"],
        "营销": ["marketing", "copy", "seo", "campaign"],
    }
    for trigger, mapped_terms in keyword_map.items():
        if trigger in lower:
            terms.extend(mapped_terms)

    deduped = []
    seen = set()
    for term in terms:
        cleaned = term.strip()
        key = cleaned.lower()
        if cleaned and key not in seen:
            seen.add(key)
            deduped.append(cleaned)
    return deduped


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug or f"ai-skill-{uuid4().hex[:8]}")[:80]
