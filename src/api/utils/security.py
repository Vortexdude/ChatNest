#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jwt
from .temp import Deps
from src.config import settings
from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.api.exceptions.exceptions import TokenError


__all__ = ["JWTUtil"]

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class JWTUtil:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_text: str, hashed_pass: str):
        return pwd_context.verify(plain_text, hashed_pass)

    @staticmethod
    def create_access_token(data: dict, expire_delta: timedelta | None = None, **kwargs):
        to_encode = data.copy()
        if expire_delta:
            expire = datetime.now() + expire_delta
        else:
            expire = datetime.now() + timedelta(seconds=settings.TOKEN_EXPIRE_SECONDS)

        to_encode.update({'exp': expire, **kwargs})
        token = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
        return token


    @staticmethod
    async def jwt_authentication(container, token: str):
        user_id = _decode_token(token)

        user = Deps(container).fetch_user(user_id)
        if not user:
            raise TokenError(msg="Invalid Token")
        print(user.to_dict())
        return user


def _decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload['user_id']
        if not user_id:
            raise TokenError(msg="Invalid Token")
    except jwt.exceptions.ExpiredSignatureError:
        raise TokenError(msg="Token is expired")

    except (jwt.exceptions.PyJWTError, Exception):
        raise TokenError(msg="Invalid Token")

    return user_id
