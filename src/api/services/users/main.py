from .repository import UserRepository
from src.api.exceptions.errors import NotFountError
from fastapi import Response


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_users(self):
        return self._user_repository.get_all()

    def get_user_by_id(self, user_id: str):
        return self._user_repository.get_by_id(user_id)

    def create_user(self, data):
        try:
            entity = self._user_repository.get_by_name(data.username)
            if entity:
                return {"status": "user already exits"}
            entity = self._user_repository.get_by_email(data.email)
            if entity:
                return {"status": "user already exits"}
        except NotFountError:
            return self._user_repository.add(data)

    def delete_by_user_id(self, user_id: str):
        try:
            self._user_repository.delete_by_id(user_id)
        except NotFountError:
            return Response(status_code=404)
        else:
            return Response(status_code=204)
