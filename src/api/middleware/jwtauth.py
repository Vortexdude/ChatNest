#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any
from fastapi import Request, status
from src.api.utils.security import JWTUtil
from src.api.utils.containers import Container
from src.api.utils.routes import by_pass_route
from src.api.exceptions.exceptions import TokenError
from dependency_injector.wiring import inject, Provide
from starlette.authentication import (
    AuthenticationBackend, AuthCredentials, AuthenticationError, SimpleUser
)


@inject
def get_user(user_id: str, user_service = Provide[Container.user_service]):
    return user_service.get_user_by_id(user_id)


class _AuthError(AuthenticationError):
    def __init__(self, *, code: int = None, msg: str = None, headers: dict[str, Any] = None):
        self.code = code
        self.msg = msg
        self.headers = headers


class JWTAuthMiddleware(AuthenticationBackend):

    async def authenticate(self, request: Request):
        if by_pass_route(request.url.path):
            return

        auth = request.headers.get("Authorization")
        if not auth:
            raise _AuthError(
                code=status.HTTP_401_UNAUTHORIZED,
                msg="Authorization token is required",
                headers={"WWW-Authenticated": "Bearer"}
            )

        scheme, token = auth.split()
        if scheme.lower() != 'bearer':
            return
        try:
            user_id = JWTUtil.decode_token(token=token)
            user = get_user(user_id)

        except TokenError as exc:
            raise _AuthError(code=exc.code, msg=exc.msg, headers=exc.headers)

        except Exception as e:
            raise _AuthError(
                code=getattr(e, 'code', 500),
                msg=getattr(e, "msg", "Internal Server Error")
            )

        return AuthCredentials(["authenticated"]), SimpleUser(user.username)
