import logging
from src.api import FastAPI
from src.config import Setting
from src.api.routes import router
from src.ws import router as wsrouter
from fastapi.staticfiles import StaticFiles
from src.api.utils.containers import Container
from src.web.routes import router as web_router
from src.api.middleware.jwtauth import JWTAuthMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

logger = logging.getLogger(__name__)


def settle_files(app, static_dir='src/static'):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")



def register_app() -> FastAPI:
    container = Container()
    container.config.from_dict(Setting().model_dump())
    db = container.db()
    db.create_database()
    # https://github.com/pyca/bcrypt/issues/684#issuecomment-1858400267
    logging.getLogger('passlib').setLevel(logging.ERROR)

    app = FastAPI(container=container)
    settle_files(app)
    app.container = container
    app.add_middleware(AuthenticationMiddleware, backend=JWTAuthMiddleware())
    app.include_router(router, prefix=container.config.API_VERSION_STR())
    app.include_router(wsrouter, prefix="/ws")
    app.include_router(web_router)

    return app
