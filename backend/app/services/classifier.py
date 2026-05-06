import re
from typing import Optional, Tuple

from app.models.category import CategoryRead
from app.models.chat import ParsedLearning
from app.models.skill import SkillRead


KEYWORDS = {
    "craft": [
        "app",
        "build",
        "code",
        "debug",
        "design",
        "draft",
        "generate",
        "implement",
        "javascript",
        "prototype",
        "python",
        "react",
        "ui",
        "ux",
        "write",
        "website",
    ],
    "theory": [
        "analysis",
        "analyze",
        "compare",
        "concept",
        "data",
        "evaluate",
        "explain",
        "insight",
        "logic",
        "math",
        "metric",
        "model",
        "reason",
        "research",
        "summarize",
    ],
    "life": [
        "agent",
        "automate",
        "deploy",
        "integrate",
        "monitor",
        "ops",
        "operation",
        "pipeline",
        "process",
        "schedule",
        "script",
        "sync",
        "task",
        "workflow",
    ],
}

LEARNED_SIGNALS = (
    "today i learned",
    "i learned",
    "learned",
    "i have learned",
    "i mastered",
    "i can now",
    "i got good at",
    "我学会",
    "我已经学会",
    "我会了",
    "我掌握了",
    "我搞懂了",
)

PLAN_SIGNALS = (
    "i want to learn",
    "i want to build",
    "i want to do",
    "i plan to",
    "how can i",
    "help me",
    "我要学",
    "我想学",
    "我想做",
    "我准备做",
    "我打算做",
    "怎么做",
)

STOP_WORDS = {
    "a",
    "an",
    "and",
    "at",
    "by",
    "for",
    "from",
    "i",
    "in",
    "into",
    "is",
    "it",
    "learn",
    "learned",
    "learning",
    "my",
    "of",
    "on",
    "or",
    "skill",
    "skills",
    "that",
    "the",
    "to",
    "want",
    "with",
}


def classify_learning_text(text: str, categories: list[CategoryRead]) -> ParsedLearning:
    category_ids = {category.id for category in categories}
    lowered = text.lower()

    category_id = categories[0].id if categories else "craft"
    matched_dynamic = False
    for category in categories:
        label_tokens = [token for token in re.split(r"[^a-z0-9]+", category.label.lower()) if len(token) >= 2]
        if category.id.startswith("ai-") and "ai" in lowered:
            if any(token in lowered for token in label_tokens if token != "ai"):
                category_id = category.id
                matched_dynamic = True
                break
            if category.id == "ai-ppt" and any(token in lowered for token in ("ppt", "slides", "presentation", "deck")):
                category_id = category.id
                matched_dynamic = True
                break

    if not matched_dynamic:
        for candidate_id, words in KEYWORDS.items():
            if candidate_id in category_ids and any(word in lowered for word in words):
                category_id = candidate_id
                break

    return ParsedLearning(
        name=_short_name(text),
        category_id=category_id,
        one_line="Logged to the orbit.",
    )


def detect_chat_intent(text: str) -> str:
    lowered = text.lower().strip()
    if any(signal in lowered for signal in LEARNED_SIGNALS):
        return "learned_skill"
    if any(signal in lowered for signal in PLAN_SIGNALS):
        return "goal_planning"
    # Questions are usually planning-oriented for this assistant.
    if "?" in text or "？" in text:
        return "goal_planning"
    return "learned_skill"


def suggest_skill_combos(text: str, skills: list[SkillRead], limit: int = 3) -> list[dict]:
    if not skills:
        return []
    goal_tokens = _keywords(text)
    scored: list[tuple[float, SkillRead]] = []
    for skill in skills:
        skill_tokens = _keywords(f"{skill.name} {skill.note or ''} {skill.source_text or ''}")
        overlap = len(goal_tokens & skill_tokens)
        # Keep a small base score so sparse text still returns usable combos.
        score = overlap + (0.25 if skill.source_text else 0.0)
        scored.append((score, skill))

    scored.sort(key=lambda pair: (pair[0], pair[1].updated_at), reverse=True)
    anchors = [skill for score, skill in scored if score > 0][:limit]
    if not anchors:
        anchors = [skill for _, skill in scored[:limit]]

    suggestions: list[dict] = []
    used_ids: set[str] = set()
    for anchor in anchors:
        combo = [anchor]
        used_ids.add(anchor.id)
        # Add one complementary skill from a different category.
        companion = next(
            (
                candidate
                for _, candidate in scored
                if candidate.id not in used_ids and candidate.category_id != anchor.category_id
            ),
            None,
        )
        if companion:
            combo.append(companion)
            used_ids.add(companion.id)

        suggestions.append(
            {
                "title": " + ".join(item.name for item in combo),
                "reason": _combo_reason(text, combo),
                "skills": combo,
            }
        )
    return suggestions


def infer_new_category(text: str, categories: list[CategoryRead]) -> Optional[Tuple[str, str]]:
    lowered = text.lower()
    existing_ids = {category.id for category in categories}
    existing_labels = {category.label.lower() for category in categories}

    # High-confidence shortcut for the user's main scenario.
    if "ai" in lowered and any(token in lowered for token in ("ppt", "slides", "presentation", "deck")):
        if "ai-ppt" not in existing_ids and "ai ppt" not in existing_labels:
            return ("ai-ppt", "AI PPT")
        return None

    match = re.search(r"\bai[\s:：\-_/]+([a-z0-9][a-z0-9\s\-/]{1,20})", lowered)
    if not match:
        return None

    tail = " ".join(match.group(1).split())
    tail = re.sub(r"[^a-z0-9\s\-]", "", tail).strip(" -")
    if len(tail) < 2:
        return None

    label = f"AI {tail.title()}"
    category_id = _slugify(label)
    if category_id in existing_ids or label.lower() in existing_labels:
        return None
    return (category_id, label)


def _short_name(text: str) -> str:
    cleaned = " ".join(text.strip().split())
    prefixes = ("today i learned ", "i learned ", "learned ")
    lowered = cleaned.lower()
    for prefix in prefixes:
        if lowered.startswith(prefix):
            cleaned = cleaned[len(prefix) :]
            break
    return cleaned[:80] or "Untitled skill"


def _keywords(text: str) -> set[str]:
    chunks = []
    current = []
    for ch in text.lower():
        if ch.isalnum():
            current.append(ch)
        else:
            if current:
                chunks.append("".join(current))
                current = []
    if current:
        chunks.append("".join(current))
    return {token for token in chunks if len(token) >= 3 and token not in STOP_WORDS}


def _combo_reason(goal_text: str, combo: list[SkillRead]) -> str:
    goal = _short_name(goal_text)
    if len(combo) == 1:
        return f"Start with `{combo[0].name}` as your first lever for '{goal}'."
    return (
        f"Use `{combo[0].name}` for core execution, and pair with `{combo[1].name}` "
        f"to improve delivery quality for '{goal}'."
    )


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return cleaned[:48] or "ai-custom"
