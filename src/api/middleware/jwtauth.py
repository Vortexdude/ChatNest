from starlette.authentication import AuthenticationBackend, AuthCredentials
from src.api.utils.security import JWTUtil
from fastapi import Request

skip_urls = [
    "/api/v1/login",
    "/api/v1/register",
    "/api/v1/docs",
    "/api/v1/redocs",
]

class JWTAuthMiddleware(AuthenticationBackend):

    def authenticate(self, request: Request):
        auth = request.headers.get("Authorization")
        if not auth:
            return
        if request.url.path in skip_urls:
            return

        scheme, token = auth.split()
        if scheme.lower() != 'bearer':
            return

        user = JWTUtil.jwt_authentication(token)
        return AuthCredentials(['authenticated']), user
