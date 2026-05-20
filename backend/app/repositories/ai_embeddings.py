from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import AIEmbeddingRecord, AILibraryItemRecord, AISkillRecord
from app.models.ai_embedding import AIEmbeddingSearchResult, AIRecommendedPlan
from app.repositories.ai_library import _loads as _loads_library
from app.repositories.ai_library import _to_read as _library_to_read
from app.repositories.ai_skills import _loads as _loads_skill
from app.repositories.ai_skills import _to_read as _skill_to_read
from app.services.embeddings import EmbeddingClient, cosine_similarity
from app.services.semantic_intents import intent_ids, intent_profile


def ensure_ai_embedding_seed(db: Session) -> None:
    client = EmbeddingClient()
    docs = [*_skill_documents(db), *_library_documents(db)]
    active_keys = {(doc["source_type"], doc["source_id"]) for doc in docs}
    existing = {
        (record.source_type, record.source_id): record
        for record in db.scalars(select(AIEmbeddingRecord)).all()
    }
    now = datetime.now(timezone.utc)

    for doc in docs:
        key = (doc["source_type"], doc["source_id"])
        content_hash = hashlib.sha256(doc["content"].encode("utf-8")).hexdigest()
        record = existing.get(key)
        should_embed = (
            record is None
            or record.content_hash != content_hash
            or record.embedding_provider != client.provider
            or record.embedding_model != client.model
            or record.embedding_dimension != len(json.loads(record.embedding_json or "[]"))
        )
        if should_embed:
            embedding = client.embed(doc["content"])
            if record is None:
                record = AIEmbeddingRecord(
                    id=f"{doc['source_type']}:{doc['source_id']}"[:120],
                    source_id=doc["source_id"],
                    source_type=doc["source_type"],
                    created_at=now,
                    updated_at=now,
                    content_hash=content_hash,
                )
                db.add(record)
            _apply_document(record, doc, embedding, client, content_hash, now)
        elif record:
            _apply_document_metadata(record, doc, now)

    for key, record in existing.items():
        if key not in active_keys:
            db.delete(record)
    db.commit()


def search_ai_knowledge(
    db: Session,
    query: str,
    source_types: list[str] | None = None,
    top_k: int = 8,
    threshold: float | None = None,
) -> list[AIEmbeddingSearchResult]:
    threshold = settings.ai_search_default_threshold if threshold is None else threshold
    client = EmbeddingClient()
    query_embedding = client.embed(query)

    stmt = select(AIEmbeddingRecord)
    if source_types:
        stmt = stmt.where(AIEmbeddingRecord.source_type.in_(source_types))

    scored: list[tuple[float, AIEmbeddingRecord]] = []
    for record in db.scalars(stmt).all():
        try:
            embedding = json.loads(record.embedding_json or "[]")
        except json.JSONDecodeError:
            continue
        score = cosine_similarity(query_embedding, embedding)
        final_score = _semantic_score(score, query, record)
        if final_score >= threshold:
            scored.append((final_score, record))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [_to_result(db, record, score) for score, record in scored[:top_k]]


def compose_ai_recommendations(db: Session, query: str, top_k: int = 5, threshold: float | None = None) -> tuple[list[AIEmbeddingSearchResult], list[AIEmbeddingSearchResult]]:
    recommendations = search_ai_knowledge(
        db,
        query=query,
        source_types=["combination", "workflow"],
        top_k=top_k,
        threshold=threshold,
    )
    supporting_skills = search_ai_knowledge(
        db,
        query=query,
        source_types=["skill"],
        top_k=5,
        threshold=max(0.16, (threshold if threshold is not None else settings.ai_search_default_threshold) - 0.06),
    )
    return recommendations, supporting_skills


def recommend_ai_plans(db: Session, query: str, top_k: int = 3, threshold: float | None = None) -> tuple[list[str], list[AIRecommendedPlan], list[AIEmbeddingSearchResult]]:
    candidates = search_ai_knowledge(
        db,
        query=query,
        source_types=["combination", "workflow"],
        top_k=24,
        threshold=threshold,
    )
    query_intents = intent_ids(query, limit=4)
    supporting_skills = search_ai_knowledge(
        db,
        query=query,
        source_types=["skill"],
        top_k=5,
        threshold=max(0.16, (threshold if threshold is not None else settings.ai_search_default_threshold) - 0.06),
    )
    plans = _pick_recommended_plans(query, query_intents, candidates, top_k)
    return query_intents, plans, supporting_skills


def _skill_documents(db: Session) -> list[dict]:
    docs = []
    for skill in db.scalars(select(AISkillRecord).where(AISkillRecord.is_active.is_(True))).all():
        tags = _loads_skill(skill.tags_json)
        examples = _loads_skill(skill.examples_json)
        content = "\n".join(
            value
            for value in [
                f"Skill: {skill.name}",
                f"Category: {skill.category_label}",
                f"Subcategory: {skill.sub_skill_label}",
                f"Tool: {skill.tool}",
                f"Stage: {skill.stage}",
                f"Description: {skill.description}",
                f"Tags: {', '.join(tags)}",
                f"Examples: {'; '.join(examples)}",
            ]
            if value.strip()
        )
        profile = intent_profile(
            skill.name,
            [skill.category_label, skill.sub_skill_label, skill.tool, skill.stage, skill.description, " ".join(tags), " ".join(examples)],
        )
        content = _with_profile(content, profile)
        docs.append(
            {
                "source_id": skill.id,
                "source_type": "skill",
                "title": skill.name,
                "category_id": skill.category_id,
                "category_label": skill.category_label,
                "sub_skill_id": skill.sub_skill_id,
                "sub_skill_label": skill.sub_skill_label,
                "content": content,
                "metadata": {
                    "summary": skill.description,
                    "tools": [skill.tool] if skill.tool else [],
                    "tags": tags,
                    "importance": skill.importance,
                    **profile,
                },
            }
        )
    return docs


def _library_documents(db: Session) -> list[dict]:
    docs = []
    for item in db.scalars(select(AILibraryItemRecord).where(AILibraryItemRecord.is_active.is_(True))).all():
        tools = _loads_library(item.tools_json)
        steps = _loads_library(item.steps_json)
        outputs = _loads_library(item.outputs_json)
        tags = _loads_library(item.tags_json)
        content = "\n".join(
            value
            for value in [
                f"{item.item_type.title()}: {item.title}",
                f"Category: {item.category_label}",
                f"Subcategory: {item.sub_skill_label}",
                f"Summary: {item.summary}",
                f"Tools: {', '.join(tools)}",
                f"Steps: {'; '.join(steps)}",
                f"Outputs: {', '.join(outputs)}",
                f"Tags: {', '.join(tags)}",
                f"Source: {item.source_section}",
            ]
            if value.strip()
        )
        profile = intent_profile(
            item.title,
            [item.category_label, item.sub_skill_label, item.summary, " ".join(tools), " ".join(steps), " ".join(outputs), " ".join(tags), item.source_section],
        )
        content = _with_profile(content, profile)
        docs.append(
            {
                "source_id": item.id,
                "source_type": item.item_type,
                "title": item.title,
                "category_id": item.category_id,
                "category_label": item.category_label,
                "sub_skill_id": item.sub_skill_id,
                "sub_skill_label": item.sub_skill_label,
                "content": content,
                "metadata": {
                    "summary": item.summary,
                    "tools": tools,
                    "steps": steps,
                    "outputs": outputs,
                    "tags": tags,
                    "importance": item.importance,
                    **profile,
                },
            }
        )
    return docs


def _apply_document(record: AIEmbeddingRecord, doc: dict, embedding: list[float], client: EmbeddingClient, content_hash: str, now: datetime) -> None:
    _apply_document_metadata(record, doc, now)
    record.embedding_json = json.dumps(embedding)
    record.content_hash = content_hash
    record.embedding_provider = client.provider
    record.embedding_model = client.model
    record.embedding_dimension = len(embedding)


def _apply_document_metadata(record: AIEmbeddingRecord, doc: dict, now: datetime) -> None:
    record.title = doc["title"]
    record.category_id = doc["category_id"]
    record.category_label = doc["category_label"]
    record.sub_skill_id = doc["sub_skill_id"]
    record.sub_skill_label = doc["sub_skill_label"]
    record.content = doc["content"]
    record.metadata_json = json.dumps(doc["metadata"], ensure_ascii=False)
    record.updated_at = now


def _semantic_score(score: float, query: str, record: AIEmbeddingRecord) -> float:
    hay = f"{record.title} {record.content}".lower()
    title_text = record.title.lower()
    title_hay = f"{record.title} {record.sub_skill_label} {record.category_label}".lower()
    lowered = query.lower()
    query_intents = set(intent_ids(query, limit=4))
    metadata = _loads_metadata(record.metadata_json)
    record_intents = set(metadata.get("intents", []))
    bonus = 0.0
    if query_intents and record_intents:
        overlap = len(query_intents & record_intents)
        if overlap:
            bonus += 0.26 + 0.06 * (overlap - 1)
        else:
            bonus -= 0.18
    if "presentation_deck" in query_intents and "presentation_deck" not in record_intents:
        bonus -= 0.2
    if "presentation_deck" in query_intents:
        direct_title_match = any(token in title_text for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        title_match = direct_title_match or any(token in title_hay for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        content_match = any(token in hay for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        focused_query = not any(token in lowered for token in ("研究", "调研", "report", "research", "数据", "data", "图", "design", "社媒", "海报"))
        if direct_title_match:
            bonus += 0.36
        elif title_match:
            bonus += 0.12
        elif content_match:
            bonus += 0.04
        if focused_query and not direct_title_match:
            bonus -= 0.16
    if any(token in lowered for token in ("ppt", "演示", "演示文档", "演示稿", "幻灯", "汇报", "提案")) and any(token in hay for token in ("ppt", "slides", "deck", "gamma", "beautiful.ai", "幻灯", "演示", "提案")):
        bonus += 0.12
    if any(token in lowered for token in ("报告", "report", "研究")) and any(token in hay for token in ("report", "research", "报告", "研究", "研报")):
        bonus += 0.08
    if any(token in lowered for token in ("代码", "code", "编程")) and any(token in hay for token in ("code", "coding", "cursor", "claude code", "编程")):
        bonus += 0.08
    if record.source_type == "workflow":
        bonus += 0.035
    try:
        importance = float(metadata.get("importance", 0))
    except (TypeError, ValueError):
        importance = 0.0
    return score * 0.72 + bonus + min(importance, 100.0) / 1000.0


def _to_result(db: Session, record: AIEmbeddingRecord, score: float) -> AIEmbeddingSearchResult:
    metadata = _loads_metadata(record.metadata_json)
    item = None
    if record.source_type == "skill":
        skill = db.get(AISkillRecord, record.source_id)
        item = _skill_to_read(skill) if skill else None
    elif record.source_type in {"combination", "workflow"}:
        library = db.get(AILibraryItemRecord, record.source_id)
        item = _library_to_read(library) if library else None
    return AIEmbeddingSearchResult(
        source_id=record.source_id,
        source_type=record.source_type,
        score=round(score, 4),
        title=record.title,
        category_id=record.category_id,
        category_label=record.category_label,
        sub_skill_id=record.sub_skill_id,
        sub_skill_label=record.sub_skill_label,
        summary=metadata.get("summary", ""),
        tools=metadata.get("tools", []),
        steps=metadata.get("steps", []),
        outputs=metadata.get("outputs", []),
        tags=metadata.get("tags", []),
        item=item,
    )


def _pick_recommended_plans(query: str, query_intents: list[str], candidates: list[AIEmbeddingSearchResult], top_k: int) -> list[AIRecommendedPlan]:
    if not candidates:
        return []

    ranked = []
    for candidate in candidates:
        profile = _recommendation_profile(candidate)
        fit = _plan_fit_score(query, query_intents, candidate, profile)
        ranked.append((fit, profile, candidate))
    ranked.sort(key=lambda item: item[0], reverse=True)

    slots = _plan_slots(query, query_intents)
    plans: list[AIRecommendedPlan] = []
    used_ids: set[str] = set()
    for slot in slots:
        best = None
        for base_score, profile, candidate in ranked:
            if candidate.source_id in used_ids:
                continue
            slot_score = base_score + _slot_bonus(slot["id"], candidate, profile)
            if best is None or slot_score > best[0]:
                best = (slot_score, profile, candidate)
        if best is None:
            continue
        score, profile, candidate = best
        used_ids.add(candidate.source_id)
        plans.append(
            AIRecommendedPlan(
                plan_type=slot["id"],
                label=slot["label"],
                reason=_reason_for_plan(slot["id"], candidate, profile),
                best_for=profile["best_for"],
                tradeoff=profile["tradeoff"],
                required_inputs=profile["required_inputs"],
                expected_outputs=profile["expected_outputs"],
                score=round(score, 4),
                recommendation=candidate,
            )
        )
        if len(plans) >= top_k:
            break
    return plans


def _plan_slots(query: str, query_intents: list[str]) -> list[dict[str, str]]:
    lowered = query.lower()
    slots = [{"id": "fastest", "label": "Fastest path"}]
    if "presentation_deck" in query_intents:
        slots.extend(
            [
                {"id": "best_visual", "label": "Best visual deck"},
                {"id": "business_ready", "label": "Business-ready proposal"},
            ]
        )
    elif "coding_build" in query_intents:
        slots.extend(
            [
                {"id": "prototype", "label": "Prototype first"},
                {"id": "production", "label": "Production-ready build"},
            ]
        )
    elif "research_report" in query_intents:
        slots.extend(
            [
                {"id": "evidence_based", "label": "Most evidence-based"},
                {"id": "presentation_ready", "label": "Report to deck"},
            ]
        )
    elif "visual_design" in query_intents:
        slots.extend(
            [
                {"id": "best_visual", "label": "Best visual quality"},
                {"id": "brand_ready", "label": "Brand-ready assets"},
            ]
        )
    else:
        slots.extend(
            [
                {"id": "balanced", "label": "Balanced choice"},
                {"id": "highest_quality", "label": "Highest quality"},
            ]
        )

    if any(token in lowered for token in ("简单", "新手", "容易", "不要复杂", "easy", "beginner")):
        slots.insert(1, {"id": "easiest", "label": "Easiest for beginners"})
    return slots


def _recommendation_profile(candidate: AIEmbeddingSearchResult) -> dict:
    text = " ".join(
        [
            candidate.title,
            candidate.summary,
            candidate.category_label,
            candidate.sub_skill_label,
            " ".join(candidate.tools),
            " ".join(candidate.steps),
            " ".join(candidate.outputs),
            " ".join(candidate.tags),
        ]
    ).lower()
    tool_count = len(candidate.tools)
    step_count = len(candidate.steps)
    is_ppt = any(token in text for token in ("ppt", "presentation", "slides", "deck", "gamma", "canva", "演示", "幻灯", "汇报", "提案"))
    is_research = any(token in text for token in ("research", "perplexity", "notebooklm", "elicit", "调研", "研究", "报告", "研报", "文献"))
    is_visual = any(token in text for token in ("canva", "gamma", "beautiful.ai", "figma", "midjourney", "recraft", "visual", "设计", "视觉"))
    is_business = any(token in text for token in ("pitch", "proposal", "sales", "crm", "close", "hubspot", "business", "商业", "客户", "提案", "销售"))
    is_code = any(token in text for token in ("code", "cursor", "claude code", "github", "react", "api", "代码", "编程", "开发"))

    speed = "fast" if tool_count <= 3 and step_count <= 3 else "medium" if tool_count <= 5 else "deep"
    difficulty = "beginner" if tool_count <= 3 and not is_code else "intermediate" if tool_count <= 5 else "advanced"
    quality = "professional" if is_research or is_visual or is_business or candidate.source_type == "workflow" else "draft"

    outputs = candidate.outputs[:] or _infer_outputs(is_ppt, is_research, is_visual, is_business, is_code)
    inputs = _infer_inputs(is_ppt, is_research, is_visual, is_business, is_code)
    best_for = _best_for(candidate, is_ppt, is_research, is_visual, is_business, is_code, speed)
    tradeoff = _tradeoff(speed, difficulty, quality)
    return {
        "speed": speed,
        "difficulty": difficulty,
        "quality": quality,
        "is_ppt": is_ppt,
        "is_research": is_research,
        "is_visual": is_visual,
        "is_business": is_business,
        "is_code": is_code,
        "best_for": best_for,
        "tradeoff": tradeoff,
        "required_inputs": inputs,
        "expected_outputs": outputs,
    }


def _plan_fit_score(query: str, query_intents: list[str], candidate: AIEmbeddingSearchResult, profile: dict) -> float:
    score = candidate.score
    if "presentation_deck" in query_intents and profile["is_ppt"]:
        score += 0.32
    if "research_report" in query_intents and profile["is_research"]:
        score += 0.28
    if "coding_build" in query_intents and profile["is_code"]:
        score += 0.28
    if "visual_design" in query_intents and profile["is_visual"]:
        score += 0.24
    lowered = query.lower()
    if any(token in lowered for token in ("快", "快速", "马上", "today", "fast")) and profile["speed"] == "fast":
        score += 0.18
    if any(token in lowered for token in ("好看", "设计", "视觉", "beautiful", "visual")) and profile["is_visual"]:
        score += 0.18
    if any(token in lowered for token in ("商业", "客户", "pitch", "提案", "proposal")) and profile["is_business"]:
        score += 0.18
    if any(token in lowered for token in ("简单", "新手", "easy", "beginner")) and profile["difficulty"] == "beginner":
        score += 0.15
    return score


def _slot_bonus(slot_id: str, candidate: AIEmbeddingSearchResult, profile: dict) -> float:
    bonus = 0.0
    if slot_id == "fastest":
        bonus += 0.28 if profile["speed"] == "fast" else 0.08 if profile["speed"] == "medium" else -0.08
    elif slot_id == "easiest":
        bonus += 0.25 if profile["difficulty"] == "beginner" else -0.04
    elif slot_id in {"best_visual", "brand_ready"}:
        bonus += 0.28 if profile["is_visual"] else -0.08
    elif slot_id in {"business_ready", "production"}:
        bonus += 0.25 if profile["is_business"] or profile["quality"] == "professional" else -0.04
    elif slot_id == "prototype":
        bonus += 0.22 if profile["speed"] in {"fast", "medium"} else 0.0
    elif slot_id == "evidence_based":
        bonus += 0.28 if profile["is_research"] else -0.08
    elif slot_id == "presentation_ready":
        bonus += 0.18 if profile["is_ppt"] else 0.0
    elif slot_id == "highest_quality":
        bonus += 0.18 if profile["quality"] == "professional" else 0.0
    return bonus


def _reason_for_plan(slot_id: str, candidate: AIEmbeddingSearchResult, profile: dict) -> str:
    tools = " + ".join(candidate.tools[:4]) if candidate.tools else candidate.title
    if slot_id == "fastest":
        return f"{tools} has a short tool chain and can produce a usable first version quickly."
    if slot_id == "best_visual":
        return f"{tools} is stronger for layout, visual polish, and presentation-ready design."
    if slot_id == "business_ready":
        return f"{tools} fits a more polished proposal or client-facing business deck."
    if slot_id == "easiest":
        return f"{tools} is simpler to operate and works well when you want fewer steps."
    if slot_id == "evidence_based":
        return f"{tools} is better when the result needs sources, research, and structured reasoning."
    if slot_id == "prototype":
        return f"{tools} is useful for getting a working prototype before hardening details."
    return f"{tools} gives a balanced path for this task with {profile['quality']} output potential."


def _infer_inputs(is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool) -> list[str]:
    if is_ppt:
        return ["topic or goal", "target audience", "rough outline or source material", "preferred style"]
    if is_research:
        return ["research question", "scope", "source requirements", "output format"]
    if is_code:
        return ["feature goal", "tech stack", "repo or mockup", "acceptance criteria"]
    if is_visual:
        return ["brand/style reference", "copy or prompt", "format size", "example visuals"]
    if is_business:
        return ["customer segment", "offer", "channel", "success metric"]
    return ["goal", "context", "constraints", "desired output"]


def _infer_outputs(is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool) -> list[str]:
    if is_ppt:
        return ["presentation outline", "editable deck draft", "visual direction"]
    if is_research:
        return ["research brief", "source summary", "report draft"]
    if is_code:
        return ["working prototype", "code changes", "deployment checklist"]
    if is_visual:
        return ["image assets", "layout variants", "export-ready visuals"]
    if is_business:
        return ["campaign draft", "CRM or outreach plan", "customer-facing copy"]
    return ["action plan", "draft output", "next-step checklist"]


def _best_for(candidate: AIEmbeddingSearchResult, is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool, speed: str) -> str:
    if is_ppt and is_business:
        return "client-facing decks, pitch materials, and business proposals"
    if is_ppt and is_visual:
        return "presentation documents that need a cleaner visual style"
    if is_ppt:
        return "turning a topic or source material into a clear slide deck"
    if is_research:
        return "research-heavy tasks that need grounded structure and sources"
    if is_code:
        return "software prototypes, code edits, and product implementation"
    if is_visual:
        return "visual assets, layouts, and design exploration"
    return "quick execution" if speed == "fast" else "multi-step project work"


def _tradeoff(speed: str, difficulty: str, quality: str) -> str:
    if speed == "fast":
        return "Fastest route, but it may need a manual polish pass."
    if difficulty == "advanced":
        return "More powerful, but it asks for clearer inputs and more review."
    if quality == "professional":
        return "Better output quality, with a slightly longer setup."
    return "Balanced option with moderate setup and review effort."


def _with_profile(content: str, profile: dict) -> str:
    semantic_lines = [
        f"Semantic intents: {', '.join(profile.get('intents', []))}",
        f"Meaning: {'; '.join(profile.get('semantic_labels', []))}",
        f"Use cases: {'; '.join(profile.get('use_cases', []))}",
        f"Equivalent user wording: {', '.join(profile.get('expanded_terms', []))}",
    ]
    return "\n".join([content, *[line for line in semantic_lines if line.split(': ', 1)[-1].strip()]])


def _loads_metadata(raw: str) -> dict:
    try:
        value = json.loads(raw or "{}")
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}
