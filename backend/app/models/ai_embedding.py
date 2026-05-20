from __future__ import annotations

from pydantic import BaseModel, Field

from app.models.ai_library import AILibraryItemRead
from app.models.ai_skill import AISkillRead


class AIEmbeddingSearchResult(BaseModel):
    source_id: str
    source_type: str
    score: float
    title: str
    category_id: str = ""
    category_label: str = ""
    sub_skill_id: str = ""
    sub_skill_label: str = ""
    summary: str = ""
    tools: list[str] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    item: AILibraryItemRead | AISkillRead | None = None


class AIComposeRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    top_k: int = Field(default=5, ge=1, le=20)
    threshold: float | None = Field(default=None, ge=0, le=1)


class AIComposeResponse(BaseModel):
    query: str
    message: str
    recommendations: list[AIEmbeddingSearchResult] = Field(default_factory=list)
    supporting_skills: list[AIEmbeddingSearchResult] = Field(default_factory=list)


class AIRecommendedPlan(BaseModel):
    plan_type: str
    label: str
    reason: str
    best_for: str
    tradeoff: str = ""
    required_inputs: list[str] = Field(default_factory=list)
    expected_outputs: list[str] = Field(default_factory=list)
    score: float
    recommendation: AIEmbeddingSearchResult


class AIRecommendResponse(BaseModel):
    query: str
    message: str
    intent_ids: list[str] = Field(default_factory=list)
    plans: list[AIRecommendedPlan] = Field(default_factory=list)
    supporting_skills: list[AIEmbeddingSearchResult] = Field(default_factory=list)
