from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.api.deps import get_current_user, get_db
from app.db.models import UserRecord
from app.models.category import CategoryCreate, CategoryRead
from app.models.chat import ChatAssistRequest, ChatAssistResponse, ChatIngestRequest, ChatIngestResponse, SkillComboSuggestion
from app.repositories import database
from app.services.classifier import classify_learning_text, detect_chat_intent, infer_new_category, suggest_skill_combos

router = APIRouter()


@router.post("/ingest", response_model=ChatIngestResponse)
async def ingest_learning(
    payload: ChatIngestRequest,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> ChatIngestResponse:
    categories = database.list_categories(db)
    category = _maybe_create_category_from_text(db, payload.text, categories)
    if category:
        categories.append(category)
    parsed = classify_learning_text(payload.text, categories)
    if category:
        parsed.category_id = category.id
        parsed.one_line = f"Logged to the orbit under {category.label}."
    skill = database.create_skill(db, parsed.to_skill_create(source_text=payload.text), user_id=current_user.id)
    return ChatIngestResponse(message=parsed.one_line, skill=skill)


@router.post("/assist", response_model=ChatAssistResponse)
async def assist_chat(
    payload: ChatAssistRequest,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> ChatAssistResponse:
    categories = database.list_categories(db)
    intent = detect_chat_intent(payload.text)

    if intent == "learned_skill":
        created_category = _maybe_create_category_from_text(db, payload.text, categories)
        if created_category:
            categories.append(created_category)
        parsed = classify_learning_text(payload.text, categories)
        if created_category:
            parsed.category_id = created_category.id
            parsed.one_line = f"Logged to the orbit under {created_category.label}."
        skill = database.create_skill(db, parsed.to_skill_create(source_text=payload.text), user_id=current_user.id)
        return ChatAssistResponse(
            message=parsed.one_line,
            intent=intent,
            skill=skill,
            category=created_category,
            classified_category_id=parsed.category_id,
            combos=[],
        )

    skills = database.list_skills(db, user_id=current_user.id)
    combos_data = suggest_skill_combos(payload.text, skills)
    combos = [SkillComboSuggestion(**item) for item in combos_data]
    if combos:
        message = "Here are skill combinations from your memory orbit."
    else:
        message = "I do not have enough skill memory yet. Log a few skills first, then ask again."
    return ChatAssistResponse(
        message=message,
        intent=intent,
        skill=None,
        classified_category_id=None,
        combos=combos,
    )


def _maybe_create_category_from_text(db: Session, text: str, categories: list[CategoryRead]) -> Optional[CategoryRead]:
    inferred = infer_new_category(text, categories)
    if not inferred:
        return None

    suggested_id, label = inferred
    existing_ids = {category.id for category in categories}
    category_id = suggested_id
    suffix = 2
    while category_id in existing_ids:
        candidate = f"{suggested_id}-{suffix}"
        category_id = candidate[:48]
        suffix += 1

    # Place newly inferred categories just outside current rings.
    max_radius = max((category.radius for category in categories), default=1.5)
    radius = min(max_radius + 0.32, 5.2)
    hue = (sum(ord(ch) for ch in category_id) * 53) % 360
    color = _hsl_to_hex(hue, 0.62, 0.68)
    payload = CategoryCreate(
        id=category_id,
        label=label.upper(),
        label_cn="",
        color=color,
        radius=radius,
        tilt=(0.2, -0.15, 0.08),
        speed=0.028,
    )
    return database.create_category(db, payload)


def _hsl_to_hex(h: int, s: float, l: float) -> str:
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    if 0 <= hp < 1:
        r1, g1, b1 = c, x, 0
    elif 1 <= hp < 2:
        r1, g1, b1 = x, c, 0
    elif 2 <= hp < 3:
        r1, g1, b1 = 0, c, x
    elif 3 <= hp < 4:
        r1, g1, b1 = 0, x, c
    elif 4 <= hp < 5:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x
    m = l - c / 2
    r, g, b = int((r1 + m) * 255), int((g1 + m) * 255), int((b1 + m) * 255)
    return f"#{r:02x}{g:02x}{b:02x}"
