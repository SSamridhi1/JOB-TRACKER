"""
Application configuration.

Why this file exists:
    Centralising configuration in one place (instead of scattering
    os.environ.get() calls across the codebase) makes the app easier to
    reason about, test, and deploy. `pydantic-settings` also gives us free
    validation: if a required env var is missing, the app fails fast at
    startup instead of failing mysteriously later.

Nothing here does any work yet - it only *declares* the shape of our
configuration. Real values come from environment variables / the .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Database ---
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/job_tracker"

    # --- JWT / Auth ---
    SECRET_KEY: str = "change-me-to-a-long-random-string"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- App ---
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins_list(self) -> list[str]:
        """Turn the comma-separated CORS_ORIGINS string into a list."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]


# A single, importable instance used everywhere in the app.
# Pattern: `from app.core.config import settings`
settings = Settings()
