from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AISkillBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    category_id: str = Field(min_length=1, max_length=48)
    category_label: str = Field(min_length=1, max_length=80)
    tool: str = Field(default="", max_length=80)
    stage: str = Field(default="", max_length=40)
    description: str = Field(default="", max_length=2000)
    tags: list[str] = Field(default_factory=list)
    examples: list[str] = Field(default_factory=list)
    input_types: list[str] = Field(default_factory=list)
    output_types: list[str] = Field(default_factory=list)
    difficulty: int = Field(default=2, ge=1, le=5)
    importance: int = Field(default=50, ge=0, le=100)
    is_core: bool = False
    is_active: bool = True


class AISkillCreate(AISkillBase):
    id: Optional[str] = Field(default=None, max_length=80)


class AISkillUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=120)
    category_id: Optional[str] = Field(default=None, min_length=1, max_length=48)
    category_label: Optional[str] = Field(default=None, min_length=1, max_length=80)
    tool: Optional[str] = Field(default=None, max_length=80)
    stage: Optional[str] = Field(default=None, max_length=40)
    description: Optional[str] = Field(default=None, max_length=2000)
    tags: Optional[list[str]] = None
    examples: Optional[list[str]] = None
    input_types: Optional[list[str]] = None
    output_types: Optional[list[str]] = None
    difficulty: Optional[int] = Field(default=None, ge=1, le=5)
    importance: Optional[int] = Field(default=None, ge=0, le=100)
    is_core: Optional[bool] = None
    is_active: Optional[bool] = None


class AISkillRead(AISkillBase):
    id: str
    created_at: datetime
    updated_at: datetime
