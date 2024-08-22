from typing import Callable, Type
from sqlalchemy.orm import Session
from src.api.models import User
from contextlib import AbstractContextManager
from src.api.exceptions.errors import UserNotFoundError


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def get_all(self) -> list[Type[User]]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: str):
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def get_by_name(self, username: str):
        with self.session_factory() as session:
            user = session.query(User).filter(User.username == username).first()
            if not user:
                raise UserNotFoundError(username)
            return user

    def get_by_email(self, email: str):
        with self.session_factory() as session:
            user = session.query(User).filter(User.email == email).first()
            if not user:
                raise UserNotFoundError(email)
            return user

    def add(self, data) -> User:
        with self.session_factory() as session:
            user = User(
                username=data.username,
                email=data.email,
                hashed_password=data.password
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: str) -> None:  # later change the literal type of the user_id
        with self.session_factory() as session:
            entity: User | None = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()
