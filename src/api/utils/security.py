import jwt
from src.config import settings
from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.api.exceptions.exceptions import TokenError
from dependency_injector.wiring import Provide, inject
from .containers import Container


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
    def jwt_authentication(token: str):
        user_id = _decode_token(token)
        user = fetch_user(user_id)
        if not user:
            raise TokenError(msg="Invalid Token")
        print(user.to_dict())
        return user


@inject
def fetch_user(user_id: str):
    user_service = Provide[Container.user_service]
    return user_service.get_user_by_id(user_id)

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
