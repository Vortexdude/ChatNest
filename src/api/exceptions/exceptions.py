#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any
from starlette import status
from fastapi import HTTPException


class BaseExceptionMixing(Exception):
    code: int

    def __init__(self, *, msg: str = None, data: Any = None):
        self.msg = msg
        self.data = data


class HTTPError(HTTPException):
    def __init__(self, *, code: int, msg: Any = None, headers: dict[str, Any] | None = None):
        super().__init__(status_code=code, detail=msg, headers=headers)


class BaseHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_201_CREATED

    def __init__(self, message):
        self.status_code = self.STATUS_CODE
        self.detail = message
        super().__init__(self.status_code, detail=self.detail)


class UserNotFoundException(BaseHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND


class PasswordNotMatchException(BaseHTTPException):
    STATUS_CODE = status.HTTP_207_MULTI_STATUS


class InvalidEntries(BaseHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST


class UserAlreadyExists(BaseHTTPException):
    STATUS_CODE = status.HTTP_409_CONFLICT

class TokenError(HTTPError):
    code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *, msg: str = 'Not Authenticated', headers: dict[str, Any] | None = None):
        self.msg = msg
        super().__init__(code=self.code, msg=self.msg, headers=headers or {'WWW-Authenticate': 'Bearer'})
