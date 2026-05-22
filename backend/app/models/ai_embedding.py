from __future__ import annotations

from datetime import datetime

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
    pros: list[str] = Field(default_factory=list)
    cons: list[str] = Field(default_factory=list)
    execution_steps: list[str] = Field(default_factory=list)
    required_inputs: list[str] = Field(default_factory=list)
    expected_outputs: list[str] = Field(default_factory=list)
    score: float
    recommendation: AIEmbeddingSearchResult


class AIRecommendResponse(BaseModel):
    query: str
    message: str
    intent_ids: list[str] = Field(default_factory=list)
    plans: list[AIRecommendedPlan] = Field(default_factory=list)
    comparison: list[dict[str, str]] = Field(default_factory=list)
    supporting_skills: list[AIEmbeddingSearchResult] = Field(default_factory=list)


class AIClarificationQuestion(BaseModel):
    id: str
    question: str
    why: str = ""
    examples: list[str] = Field(default_factory=list)
    options: list[str] = Field(default_factory=list)
    allow_custom: bool = True


class AIAdviceResponse(AIRecommendResponse):
    needs_clarification: bool = False
    clarification_questions: list[AIClarificationQuestion] = Field(default_factory=list)


class AIRecommendationFeedbackCreate(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    source_id: str = Field(min_length=1, max_length=120)
    source_type: str = Field(pattern="^(skill|combination|workflow)$")
    plan_type: str = Field(default="", max_length=40)
    rating: str = Field(pattern="^(up|down|too_complex|too_slow|want_faster|want_better|used)$")
    comment: str = Field(default="", max_length=1000)


class AIRecommendationFeedbackRead(AIRecommendationFeedbackCreate):
    id: str
    user_id: str | None = None
    created_at: datetime
