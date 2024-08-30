#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.config import settings
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=settings.template_dir)

