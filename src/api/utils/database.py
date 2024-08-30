#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Callable
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from contextlib import AbstractContextManager, contextmanager
from sqlalchemy.orm import Session, sessionmaker, scoped_session

Base = declarative_base()


class Database:
    def __init__(self, db_url: str):
        self._engine = create_engine(url=db_url, echo=False)
        self._session_factory = scoped_session(
            sessionmaker(
                autoflush=False,
                autocommit=False,
                bind=self._engine
            )
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
