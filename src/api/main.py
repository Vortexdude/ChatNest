from fastapi import FastAPI
from src.config import settings, Setting
from src.api.routes import router
from src.api.utils.containers import Container
import logging
logger = logging.getLogger(__name__)


def register_app() -> FastAPI:
    container = Container()
    container.config.from_dict(Setting().model_dump())

    db = container.db()
    db.create_database()

    app = FastAPI(
        title=container.config.TITLE(),
        description=container.config.DESCRIPTION(),
        docs_url=container.config.DOCS_URL(),
        redoc_url=container.config.REDOCS_URL(),
        openapi_url=container.config.OPENAPI_URL()
    )
    app.container = container
    app.include_router(router, prefix=container.config.API_VERSION_STR())
    return app
