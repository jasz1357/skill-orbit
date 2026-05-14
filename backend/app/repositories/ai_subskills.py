from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.ai_subskill_taxonomy import AI_SUBSKILLS
from app.db.models import AISubSkillRecord


def ensure_ai_subskill_seed(db: Session) -> None:
    existing_ids = set(db.scalars(select(AISubSkillRecord.id)).all())
    now = datetime.now(timezone.utc)
    for item in AI_SUBSKILLS:
        if item["id"] in existing_ids:
            continue
        db.add(
            AISubSkillRecord(
                id=item["id"],
                category_id=item["category_id"],
                category_label=item["category_label"],
                label=item["label"],
                label_cn=item["label_cn"],
                sort_order=item["sort_order"],
                created_at=now,
                updated_at=now,
            )
        )
        existing_ids.add(item["id"])
    db.commit()
