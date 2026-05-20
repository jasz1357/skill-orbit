from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.db.session import SessionLocal
from app.repositories.ai_library import ensure_ai_library_seed
from app.repositories.ai_embeddings import ensure_ai_embedding_seed
from app.repositories.ai_skills import ensure_ai_skill_seed
from app.repositories.ai_subskills import ensure_ai_subskill_seed
from app.repositories.users import ensure_admin_user


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.on_event("startup")
    def seed_admin_user() -> None:
        db = SessionLocal()
        try:
            ensure_admin_user(
                db,
                settings.default_admin_username,
                settings.default_admin_email,
                settings.default_admin_password,
            )
            ensure_ai_subskill_seed(db)
            ensure_ai_skill_seed(db)
            ensure_ai_library_seed(db)
            ensure_ai_embedding_seed(db)
        finally:
            db.close()

    return app


app = create_app()
