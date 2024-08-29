import os
from pathlib import Path
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

load_dotenv()
project_home_path = Path(__file__).resolve().parent.parent


class PostgresSecret(BaseSettings):
    user: str
    password: str
    db: str
    host: Optional[str] = '127.0.0.1'
    port: int

    model_config = SettingsConfigDict(env_prefix="POSTGRES_", )


class DATABASE:
    @property
    def url(self):
        _pg: PostgresSecret = PostgresSecret()
        POSTGRES = {
            'user': _pg.user,
            'pw': _pg.password,
            'host': _pg.host,
            'db': _pg.db,
            'port': str(_pg.port),
        }

        return "postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES


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
    DATABASE_URL: str = DATABASE().url
    template_dir: str = 'src/web/templates'

    JWT_SECRET_KEY: str = 'ds454ew54c12e87'
    TOKEN_EXPIRE_SECONDS: int = 300
    JWT_ALGORITHM: str = 'HS256'

    PROJECT_HOME: str = os.getenv("PYTHONPATH")
    skip_routes_for_jwt_auth: list = [
        "/api/v1/login",
        "/api/v1/users",
        "/api/v1/docs",
        "/api/v1/redocs",
        "/api/v1/openapi",
        "/favicon.ico",
        "/login",
        "/register",
        "/chat",
        "/room",
        "/",
    ]

    allowed_static_files: list = [
        "static/css/*",
        "static/javaScript/*",
        "static/svgs/*"
    ]

@lru_cache
def get_settings() -> Setting:
    return Setting()


settings = get_settings()

