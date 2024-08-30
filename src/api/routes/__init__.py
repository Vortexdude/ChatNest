#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter
from importlib import import_module

ENABLE_ROUTE = ["main"]
router = APIRouter()

for route in ENABLE_ROUTE:
    module = import_module(f"src.api.routes.{route}")
    router.include_router(module.router)
