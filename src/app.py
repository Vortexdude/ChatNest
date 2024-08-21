import uvicorn
from src.api.main import register_app
from src.config import settings
app = register_app()

if __name__ == "__main__":
    try:
        config = uvicorn.Config(
            app=app,
            host=settings.SERVER_HOST,
            port=settings.SERVER_PORT
        )
        server = uvicorn.Server(config)
        server.run()
    except Exception as e:
        raise e
