from .repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_users(self):
        return self._user_repository.get_all()

    def get_user_by_id(self, user_id: int):
        return self._user_repository.get_by_id(user_id)

    def create_user(self, data):
        return self._user_repository.add(data)

    def delete_by_user_id(self, user_id: int):
        return self._user_repository.delete_by_id(user_id)