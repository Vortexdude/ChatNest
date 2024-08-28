from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from src.api.utils.containers import Container
from src.api.services.users import UserService
from src.api.exceptions.errors import NotFountError
from src.api.schema import UserCreate, UserLogin


tags = ['user_repo']
router = APIRouter(tags=tags)


@router.get("/users")
@inject
def get_list(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_users()


@router.get("/user/{user_id}")
@inject
def get_by_id(user_id: str, user_service: UserService = Depends(Provide[Container.user_service])):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFountError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(data: UserCreate, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.create_user(data)


@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete(user_id: str, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.delete_by_user_id(user_id)

@router.post("/login", status_code=status.HTTP_200_OK)
@inject
def login_user(data: UserLogin, user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.login(data)
