from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from app.models.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.models.skill import SkillCreate, SkillRead, SkillUpdate


class MemoryStore:
    def __init__(self) -> None:
        self._categories: dict[str, CategoryRead] = {}
        self._skills: dict[str, SkillRead] = {}
        self._seed_categories()
        self._seed_skills()

    def list_categories(self) -> list[CategoryRead]:
        return list(self._categories.values())

    def get_category(self, category_id: str) -> Optional[CategoryRead]:
        return self._categories.get(category_id)

    def create_category(self, payload: CategoryCreate) -> CategoryRead:
        category_id = payload.id or f"cat_{uuid4().hex[:10]}"
        category = CategoryRead(id=category_id, **payload.model_dump(exclude={"id"}))
        self._categories[category_id] = category
        return category

    def update_category(self, category_id: str, payload: CategoryUpdate) -> Optional[CategoryRead]:
        category = self._categories.get(category_id)
        if not category:
            return None
        data = category.model_dump()
        data.update(payload.model_dump(exclude_unset=True))
        updated = CategoryRead(**data)
        self._categories[category_id] = updated
        return updated

    def delete_category(self, category_id: str) -> bool:
        if category_id not in self._categories or len(self._categories) <= 1:
            return False
        fallback_id = next(key for key in self._categories if key != category_id)
        for skill in list(self._skills.values()):
            if skill.category_id == category_id:
                self.update_skill(skill.id, SkillUpdate(category_id=fallback_id))
        del self._categories[category_id]
        return True

    def list_skills(self, query: Optional[str] = None, category_id: Optional[str] = None) -> list[SkillRead]:
        skills = list(self._skills.values())
        if category_id:
            skills = [skill for skill in skills if skill.category_id == category_id]
        if query:
            q = query.lower()
            skills = [skill for skill in skills if q in skill.name.lower() or q in skill.note.lower()]
        return sorted(skills, key=lambda skill: skill.created_at, reverse=True)

    def get_skill(self, skill_id: str) -> Optional[SkillRead]:
        return self._skills.get(skill_id)

    def create_skill(self, payload: SkillCreate) -> SkillRead:
        now = datetime.now(timezone.utc)
        skill = SkillRead(id=f"sk_{uuid4().hex[:12]}", created_at=now, updated_at=now, **payload.model_dump())
        self._skills[skill.id] = skill
        return skill

    def update_skill(self, skill_id: str, payload: SkillUpdate) -> Optional[SkillRead]:
        skill = self._skills.get(skill_id)
        if not skill:
            return None
        data = skill.model_dump()
        data.update(payload.model_dump(exclude_unset=True))
        data["updated_at"] = datetime.now(timezone.utc)
        updated = SkillRead(**data)
        self._skills[skill_id] = updated
        return updated

    def delete_skill(self, skill_id: str) -> bool:
        return self._skills.pop(skill_id, None) is not None

    def _seed_categories(self) -> None:
        defaults = [
            CategoryCreate(id="craft", label="CRAFT", label_cn="", color="#ffb066", radius=1.55, tilt=(0.3, 0.1, 0.05), speed=0.06),
            CategoryCreate(id="theory", label="THEORY", label_cn="", color="#7ed6e6", radius=1.95, tilt=(-0.55, 0.4, 0.2), speed=0.04),
            CategoryCreate(id="life", label="LIFE", label_cn="", color="#e69aa3", radius=2.4, tilt=(0.8, -0.3, 0.1), speed=0.03),
        ]
        for category in defaults:
            self.create_category(category)

    def _seed_skills(self) -> None:
        defaults = [
            ("CSS Grid subgrid layout", "craft"),
            ("useReducer for complex form state", "craft"),
            ("Caesar and substitution cipher basics", "theory"),
            ("Japanese sandwich technique", "life"),
            ("fract in WebGL shaders", "craft"),
            ("Intuition for Bayesian inference", "theory"),
            ("Water temperature curve in coffee brewing", "life"),
        ]
        for name, category_id in defaults:
            self.create_skill(SkillCreate(name=name, category_id=category_id))


store = MemoryStore()
