#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from glob import glob
from typing import Any
from src.config import settings
from fastapi import Request, status
from src.api.utils.security import JWTUtil
from starlette.authentication import AuthenticationBackend, AuthCredentials, AuthenticationError


class _AuthError(AuthenticationError):
    def __init__(self, *, code: int = None, msg: str = None, headers: dict[str, Any] = None):
        self.code = code
        self.msg = msg
        self.headers = headers

def allowed_files(files: list = settings.allowed_static_files) -> list:
    _allowed_file = []

    for directory in files:
        files = glob(directory, root_dir="src/")
        _allowed_file.extend(files)
    return _allowed_file

class JWTAuthMiddleware(AuthenticationBackend):

    def __init__(self, container):
        self.container = container


    async def authenticate(self, request: Request):
        if request.url.path in allowed_files():
            print(f"[INFO] -> Skipping route to the file access")
            return

        if request.url.path in settings.skip_routes_for_jwt_auth:
            print(f"[Warning] -> Skipping the route {request.url.path} for JWT authentication")
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

        user = await JWTUtil.jwt_authentication(container=self.container, token=token)
        return AuthCredentials(['authenticated']), user
