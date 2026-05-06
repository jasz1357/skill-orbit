from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    label: str = Field(min_length=1, max_length=32, examples=["CRAFT"])
    label_cn: str = Field(default="", max_length=32)
    color: str = Field(pattern=r"^#[0-9a-fA-F]{6}$", examples=["#ffb066"])
    radius: float = Field(gt=0, examples=[1.55])
    tilt: tuple[float, float, float] = Field(examples=[(0.3, 0.1, 0.05)])
    speed: float = Field(gt=0, examples=[0.06])


class CategoryCreate(CategoryBase):
    id: Optional[str] = Field(default=None, min_length=1, max_length=48)


class CategoryUpdate(BaseModel):
    label: Optional[str] = Field(default=None, min_length=1, max_length=32)
    label_cn: Optional[str] = Field(default=None, max_length=32)
    color: Optional[str] = Field(default=None, pattern=r"^#[0-9a-fA-F]{6}$")
    radius: Optional[float] = Field(default=None, gt=0)
    tilt: Optional[tuple[float, float, float]] = None
    speed: Optional[float] = Field(default=None, gt=0)


class CategoryRead(CategoryBase):
    id: str
