from uuid import uuid4
from src.api.utils.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Boolean, DateTime, inspect


def now_in_utc():
    return datetime.now(timezone.utc)


class SurrogatePK(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(String(80), default=lambda: str(uuid4()), primary_key=True)


class User(SurrogatePK):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=now_in_utc)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=now_in_utc, onupdate=now_in_utc,)

    def to_dict(self):
        _data: dict = {}
        for c in inspect(self).mapper.column_attrs:
            _att = getattr(self, c.key)
            if isinstance(_att, datetime):
                continue
            if "password" in c.key:
                continue

            _data[c.key] = _att
        return _data
