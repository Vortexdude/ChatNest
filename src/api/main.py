from fastapi import FastAPI
from src.config import settings
from src.api.routes import router


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL
    )
    app.include_router(router)
    return app
