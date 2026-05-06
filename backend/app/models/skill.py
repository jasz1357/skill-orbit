from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SkillBase(BaseModel):
    name: str = Field(min_length=1, max_length=80, examples=["CSS Grid subgrid layout"])
    category_id: str = Field(min_length=1, max_length=48, examples=["craft"])
    note: str = Field(default="", max_length=4000)
    source_text: Optional[str] = Field(default=None, max_length=2000)
    angle: Optional[float] = None


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=80)
    category_id: Optional[str] = Field(default=None, min_length=1, max_length=48)
    note: Optional[str] = Field(default=None, max_length=4000)
    angle: Optional[float] = None


class SkillRead(SkillBase):
    id: str
    created_at: datetime
    updated_at: datetime
