import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime
from src.config import settings

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
