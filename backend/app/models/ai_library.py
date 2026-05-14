from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AILibraryItemBase(BaseModel):
    item_type: str = Field(pattern="^(combination|workflow)$")
    title: str = Field(min_length=1, max_length=180)
    category_id: str = Field(default="", max_length=48)
    category_label: str = Field(default="", max_length=80)
    sub_skill_id: str = Field(default="", max_length=64)
    sub_skill_label: str = Field(default="", max_length=80)
    summary: str = Field(default="", max_length=3000)
    tools: list[str] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    source_section: str = Field(default="", max_length=120)
    importance: int = Field(default=50, ge=0, le=100)
    is_active: bool = True


class AILibraryItemCreate(AILibraryItemBase):
    id: Optional[str] = Field(default=None, max_length=100)


class AILibraryItemUpdate(BaseModel):
    item_type: Optional[str] = Field(default=None, pattern="^(combination|workflow)$")
    title: Optional[str] = Field(default=None, min_length=1, max_length=180)
    category_id: Optional[str] = Field(default=None, max_length=48)
    category_label: Optional[str] = Field(default=None, max_length=80)
    sub_skill_id: Optional[str] = Field(default=None, max_length=64)
    sub_skill_label: Optional[str] = Field(default=None, max_length=80)
    summary: Optional[str] = Field(default=None, max_length=3000)
    tools: Optional[list[str]] = None
    steps: Optional[list[str]] = None
    outputs: Optional[list[str]] = None
    tags: Optional[list[str]] = None
    source_section: Optional[str] = Field(default=None, max_length=120)
    importance: Optional[int] = Field(default=None, ge=0, le=100)
    is_active: Optional[bool] = None


class AILibraryItemRead(AILibraryItemBase):
    id: str
    created_at: datetime
    updated_at: datetime
