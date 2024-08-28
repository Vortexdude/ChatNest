from starlette import status
from fastapi import HTTPException


class UserNotFoundException(HTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND

    def __init__(self, message):
        self.status_code = self.STATUS_CODE
        self.detail = message
        super().__init__(self.status_code, detail=self.detail)


class PasswordNotMatchException(HTTPException):
    STATUS_CODE = status.HTTP_207_MULTI_STATUS

    def __init__(self, message):
        self.status_code = self.STATUS_CODE
        self.detail = message
        super().__init__(self.status_code, detail=self.detail)