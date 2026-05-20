from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.ai_embedding import AIComposeRequest, AIComposeResponse, AIEmbeddingSearchResult, AIRecommendResponse
from app.models.ai_library import AILibraryItemCreate, AILibraryItemRead, AILibraryItemUpdate
from app.models.ai_skill import AISkillCreate, AISkillRead, AISkillUpdate
from app.repositories import ai_embeddings
from app.repositories import ai_library
from app.repositories import ai_skills

router = APIRouter()


@router.get("", response_model=list[AISkillRead])
async def list_ai_skills(
    q: Optional[str] = None,
    category_id: Optional[str] = None,
    core: Optional[bool] = None,
    limit: int = Query(default=500, ge=1, le=2000),
    db: Session = Depends(get_db),
) -> list[AISkillRead]:
    return ai_skills.list_ai_skills(db, query=q, category_id=category_id, core=core, limit=limit)


@router.get("/core", response_model=list[AISkillRead])
async def list_core_ai_skills(db: Session = Depends(get_db)) -> list[AISkillRead]:
    return ai_skills.list_ai_skills(db, core=True, limit=120)


@router.get("/search", response_model=list[AIEmbeddingSearchResult])
async def semantic_ai_search(
    q: str = Query(min_length=1, max_length=2000),
    types: str = Query(default="combination,workflow"),
    top_k: int = Query(default=8, ge=1, le=30),
    threshold: Optional[float] = Query(default=None, ge=0, le=1),
    db: Session = Depends(get_db),
) -> list[AIEmbeddingSearchResult]:
    source_types = [item.strip() for item in types.split(",") if item.strip()]
    allowed = {"skill", "combination", "workflow"}
    if any(item not in allowed for item in source_types):
        raise HTTPException(status_code=400, detail="types must be skill, combination, or workflow")
    return ai_embeddings.search_ai_knowledge(db, query=q, source_types=source_types or None, top_k=top_k, threshold=threshold)


@router.post("/compose", response_model=AIComposeResponse)
async def compose_ai_skill_plan(payload: AIComposeRequest, db: Session = Depends(get_db)) -> AIComposeResponse:
    recommendations, supporting_skills = ai_embeddings.compose_ai_recommendations(
        db,
        query=payload.query,
        top_k=payload.top_k,
        threshold=payload.threshold,
    )
    message = (
        "I found relevant AI tool combinations for this task."
        if recommendations
        else "I could not find a strong combination yet. Try adding a more specific output or tool."
    )
    return AIComposeResponse(
        query=payload.query,
        message=message,
        recommendations=recommendations,
        supporting_skills=supporting_skills,
    )


@router.post("/recommend", response_model=AIRecommendResponse)
async def recommend_ai_skill_plans(payload: AIComposeRequest, db: Session = Depends(get_db)) -> AIRecommendResponse:
    intent_ids, plans, supporting_skills = ai_embeddings.recommend_ai_plans(
        db,
        query=payload.query,
        top_k=min(payload.top_k, 5),
        threshold=payload.threshold,
    )
    message = (
        "I found recommended AI workflow plans for this task."
        if plans
        else "I could not find a strong recommended plan yet. Try describing the desired output and constraints."
    )
    return AIRecommendResponse(
        query=payload.query,
        message=message,
        intent_ids=intent_ids,
        plans=plans,
        supporting_skills=supporting_skills,
    )


@router.get("/library", response_model=list[AILibraryItemRead])
async def list_ai_library(
    type: Optional[str] = Query(default=None, pattern="^(combination|workflow)$"),
    q: Optional[str] = None,
    category_id: Optional[str] = None,
    limit: int = Query(default=500, ge=1, le=2000),
    db: Session = Depends(get_db),
) -> list[AILibraryItemRead]:
    return ai_library.list_ai_library_items(db, item_type=type, query=q, category_id=category_id, limit=limit)


@router.get("/library/{item_id}", response_model=AILibraryItemRead)
async def get_ai_library_item(item_id: str, db: Session = Depends(get_db)) -> AILibraryItemRead:
    item = ai_library.get_ai_library_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="AI library item not found")
    return item


@router.post("/library", response_model=AILibraryItemRead, status_code=status.HTTP_201_CREATED)
async def create_ai_library_item(payload: AILibraryItemCreate, db: Session = Depends(get_db)) -> AILibraryItemRead:
    return ai_library.create_ai_library_item(db, payload)


@router.patch("/library/{item_id}", response_model=AILibraryItemRead)
async def update_ai_library_item(item_id: str, payload: AILibraryItemUpdate, db: Session = Depends(get_db)) -> AILibraryItemRead:
    item = ai_library.update_ai_library_item(db, item_id, payload)
    if not item:
        raise HTTPException(status_code=404, detail="AI library item not found")
    return item


@router.delete("/library/{item_id}", status_code=status.HTTP_200_OK)
async def delete_ai_library_item(item_id: str, db: Session = Depends(get_db)) -> None:
    deleted = ai_library.delete_ai_library_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="AI library item not found")


@router.get("/{skill_id}", response_model=AISkillRead)
async def get_ai_skill(skill_id: str, db: Session = Depends(get_db)) -> AISkillRead:
    skill = ai_skills.get_ai_skill(db, skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="AI skill not found")
    return skill


@router.post("", response_model=AISkillRead, status_code=status.HTTP_201_CREATED)
async def create_ai_skill(payload: AISkillCreate, db: Session = Depends(get_db)) -> AISkillRead:
    return ai_skills.create_ai_skill(db, payload)


@router.patch("/{skill_id}", response_model=AISkillRead)
async def update_ai_skill(skill_id: str, payload: AISkillUpdate, db: Session = Depends(get_db)) -> AISkillRead:
    skill = ai_skills.update_ai_skill(db, skill_id, payload)
    if not skill:
        raise HTTPException(status_code=404, detail="AI skill not found")
    return skill


@router.delete("/{skill_id}", status_code=status.HTTP_200_OK)
async def delete_ai_skill(skill_id: str, db: Session = Depends(get_db)) -> None:
    deleted = ai_skills.delete_ai_skill(db, skill_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="AI skill not found")
