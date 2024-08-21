from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

project_home_path = Path(__file__).resolve().parent.parent


class Setting(BaseSettings):
    """Global Settings"""
    model_config = SettingsConfigDict(env_file=f"{project_home_path}/.env", extra='ignore', env_file_encoding="utf-8")
    ENVIRONMENT: list[str] = ['dev', 'prod']

    API_VERSION_STR: str = '/api/v1'
    TITLE: str = "FastApi"  # later read by readme.md
    VERSION: str = '0.0.1'  # later read by readme.md
    DESCRIPTION: str = "chat api using fastapi framework"  # later read by readme.md
    DOCS_URL: str | None = f"{API_VERSION_STR}/docs"
    REDOCS_URL: str | None = f"{API_VERSION_STR}/redocs"
    OPENAPI_URL: str | None = f"{API_VERSION_STR}/openapi"
    SERVER_HOST: str = '0.0.0.0'
    SERVER_PORT: int = 5000
    DEBUG: bool = False


@lru_cache
def get_settings() -> Setting:
    return Setting()


settings = get_settings()

