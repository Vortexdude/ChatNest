from fastapi import APIRouter
from importlib import import_module
# from src.api.routes import main  # add the files not the route object

ENABLE_ROUTE = ["main"]
router = APIRouter()

for route in ENABLE_ROUTE:
    module = import_module(f"src.api.routes.{route}")
    router.include_router(module.router)
