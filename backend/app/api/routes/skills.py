from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.db.models import UserRecord
from app.models.skill import SkillCreate, SkillRead, SkillUpdate
from app.repositories import database

router = APIRouter()


@router.get("", response_model=list[SkillRead])
async def list_skills(
    q: Optional[str] = None,
    category_id: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> list[SkillRead]:
    return database.list_skills(db, user_id=current_user.id, query=q, category_id=category_id)


@router.post("", response_model=SkillRead, status_code=status.HTTP_201_CREATED)
async def create_skill(
    payload: SkillCreate,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> SkillRead:
    if not database.get_category(db, payload.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    return database.create_skill(db, payload, user_id=current_user.id)


@router.get("/{skill_id}", response_model=SkillRead)
async def get_skill(
    skill_id: str,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> SkillRead:
    skill = database.get_skill(db, skill_id, user_id=current_user.id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.patch("/{skill_id}", response_model=SkillRead)
async def update_skill(
    skill_id: str,
    payload: SkillUpdate,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> SkillRead:
    if payload.category_id and not database.get_category(db, payload.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")

    skill = database.update_skill(db, skill_id, payload, user_id=current_user.id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.delete("/{skill_id}", status_code=status.HTTP_200_OK)
async def delete_skill(
    skill_id: str,
    db: Session = Depends(get_db),
    current_user: UserRecord = Depends(get_current_user),
) -> None:
    deleted = database.delete_skill(db, skill_id, user_id=current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Skill not found")
