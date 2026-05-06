from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from app.models.category import CategoryRead
from app.models.skill import SkillCreate, SkillRead


class ChatIngestRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000, examples=["Today I learned FastAPI dependency injection."])


class ParsedLearning(BaseModel):
    name: str
    category_id: str
    one_line: str

    def to_skill_create(self, source_text: str) -> SkillCreate:
        return SkillCreate(name=self.name, category_id=self.category_id, source_text=source_text)


class ChatIngestResponse(BaseModel):
    message: str
    skill: SkillRead


class ChatAssistRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000, examples=["I want to learn machine learning project planning."])


class SkillComboSuggestion(BaseModel):
    title: str
    reason: str
    skills: list[SkillRead] = Field(default_factory=list)


class ChatAssistResponse(BaseModel):
    message: str
    intent: str
    skill: Optional[SkillRead] = None
    category: Optional[CategoryRead] = None
    classified_category_id: Optional[str] = None
    combos: list[SkillComboSuggestion] = Field(default_factory=list)
