from starlette import status
from fastapi import HTTPException


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
