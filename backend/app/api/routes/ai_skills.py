from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.ai_library import AILibraryItemCreate, AILibraryItemRead, AILibraryItemUpdate
from app.models.ai_skill import AISkillCreate, AISkillRead, AISkillUpdate
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
