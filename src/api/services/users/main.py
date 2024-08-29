from .repository import UserRepository
from src.api.exceptions.errors import NotFountError, UserNotFoundError
from src.api.exceptions.exceptions import PasswordNotMatchException, UserNotFoundException, InvalidEntries, UserAlreadyExists
from fastapi import Response
from src.api.utils.security import JWTUtil
from src.api.schema.users import Token

class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_users(self):
        return self._user_repository.get_all()

    def get_user_by_id(self, user_id: str):
        return self._user_repository.get_by_id(user_id)

    def create_user(self, data):
        try:
            if not data.username or not data.email or not data.password:
                raise InvalidEntries(message="Some fields are missing")

            entity = self._user_repository.get_by_name(data.username)
            if entity:
                raise UserAlreadyExists(message="user already exits")

            entity = self._user_repository.get_by_email(data.email)
            if entity:
                raise UserAlreadyExists(message="user already exits")

        except NotFountError:
            return self._user_repository.add(data)

    def delete_by_user_id(self, user_id: str):
        try:
            self._user_repository.delete_by_id(user_id)
        except NotFountError:
            return UserNotFoundException(message="Username does not exist")

        else:
            return Response(status_code=204)

    def authenticate_user(self, data):
        try:
            user = self._user_repository.get_by_email(data.email)
        except UserNotFoundError:
            raise UserNotFoundException(message="Email does not exist")

        if not JWTUtil.verify_password(plain_text=data.password, hashed_pass=user.hashed_password):
            raise PasswordNotMatchException(message="Password not matched")

        return user

    def login(self, data):
        user = self.authenticate_user(data)
        if not user:
            return

        data = user.to_dict()
        token = JWTUtil.create_access_token(data={"user_id": data['id'], "username": data['username']})
        return Token(access_token=token, type='bearer')
