"""
SCANIX AI
Production Configuration System
"""

from functools import lru_cache
from secrets import token_urlsafe
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
        case_sensitive=True,
    )

    # ==========================================================
    # APP
    # ==========================================================

    APP_NAME: str = "SCANIX AI"

    APP_VERSION: str = "1.0.0"

    ENV: Literal[
        "development",
        "staging",
        "production",
    ] = "development"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    LOG_LEVEL: str = "INFO"

    FRONTEND_URL: str = "http://localhost:3000"

    BACKEND_URL: str = "http://localhost:8000"

    # ==========================================================
    # SECURITY
    # ==========================================================

    SECRET_KEY: str = Field(
        default_factory=lambda: token_urlsafe(64)
    )

    JWT_SECRET: str = Field(
        default_factory=lambda: token_urlsafe(64)
    )

    # ==========================================================
    # AI
    # ==========================================================

    GEMINI_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    OPENROUTER_API_KEY: str = ""

    AI_DEFAULT_PROVIDER: str = "gemini"

    AI_FALLBACK_PROVIDER: str = "groq"

    # ==========================================================
    # FOOD
    # ==========================================================

    OPENFOODFACTS_BASE_URL: str = (
        "https://world.openfoodfacts.org"
    )

    USDA_API_KEY: str = ""

    SPOONACULAR_API_KEY: str = ""

    APININJAS_API_KEY: str = ""

    FATSECRET_CLIENT_ID: str = ""

    FATSECRET_CONSUMER_KEY: str = ""

    FATSECRET_CONSUMER_SECRET: str = ""

    # ==========================================================
    # RESEARCH
    # ==========================================================

    PUBMED_EMAIL: str = ""

    CROSSREF_BASE_URL: str = (
        "https://api.crossref.org"
    )

    CROSSREF_MAILTO: str = ""

    # ==========================================================
    # SAFETY
    # ==========================================================

    OPENFDA_BASE_URL: str = (
        "https://api.fda.gov"
    )

    OPENFDA_ENABLED: bool = True

    # ==========================================================
    # DATABASE
    # ==========================================================

    SUPABASE_URL: str = ""

    SUPABASE_KEY: str = ""

    SUPABASE_SERVICE_KEY: str = ""

    DATABASE_URL: str = ""

    # ==========================================================
    # OCR
    # ==========================================================

    TESSERACT_PATH: str = ""

    # ==========================================================
    # CACHE
    # ==========================================================

    REDIS_URL: str = Field(
        default="redis://localhost:6379"
    )

    # ==========================================================
    # AUTH
    # ==========================================================

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ==========================================================
    # OBSERVABILITY
    # ==========================================================

    SENTRY_DSN: str = ""

    POSTHOG_API_KEY: str = ""

    @property
    def IS_PRODUCTION(self):

        return self.ENV == "production"

    @property
    def IS_DEVELOPMENT(self):

        return self.ENV == "development"


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()