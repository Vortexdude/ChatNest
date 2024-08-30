#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .database import Database
from dependency_injector import containers, providers
from src.api.services.users import UserService, UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.api.routes.main", "src.api.middleware.jwtauth"])

    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=config.DATABASE_URL)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )
