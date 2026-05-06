from fastapi import APIRouter

from app.api.routes import auth, categories, chat, health, skills

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(skills.router, prefix="/skills", tags=["skills"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
