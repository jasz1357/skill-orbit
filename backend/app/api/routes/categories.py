from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.category import CategoryCreate, CategoryRead, CategoryUpdate
from app.repositories import database

router = APIRouter()


@router.get("", response_model=list[CategoryRead])
async def list_categories(
    db: Session = Depends(get_db),
    _current_user=Depends(get_current_user),
) -> list[CategoryRead]:
    return database.list_categories(db)


@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    _current_user=Depends(get_current_user),
) -> CategoryRead:
    category = database.create_category(db, payload)
    if not category:
        raise HTTPException(status_code=409, detail="Category already exists")
    return category


@router.patch("/{category_id}", response_model=CategoryRead)
async def update_category(
    category_id: str,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
    _current_user=Depends(get_current_user),
) -> CategoryRead:
    category = database.update_category(db, category_id, payload)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: str,
    db: Session = Depends(get_db),
    _current_user=Depends(get_current_user),
) -> None:
    deleted = database.delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
