from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Skill Orbit API"
    app_env: str = "local"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./skill_orbit.db"
    auth_secret_key: str = "change-this-local-secret"
    access_token_expire_minutes: int = 1440
    default_admin_username: str = "admin"
    default_admin_email: str = "admin@example.com"
    default_admin_password: str = "admin123"
    cors_origins_raw: str = Field(default="", alias="CORS_ORIGINS")

    @property
    def cors_origins(self) -> list[str]:
        if not self.cors_origins_raw:
            return ["*"]
        return [origin.strip() for origin in self.cors_origins_raw.split(",") if origin.strip()]


settings = Settings()
