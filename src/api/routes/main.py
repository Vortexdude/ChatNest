from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from src.api.utils.containers import Container
from src.api.services.users.main import UserService, UserRepository
from src.api.schema.users import UserResponse, UserCreate
from src.api.models.users import User

route = APIRouter()


@route.get("/users")
@inject
def get_users(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_users()
