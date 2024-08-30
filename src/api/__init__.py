"""
Injecting the title, description, and other parameter to the fastapi module
using the dependency_injection module
"""

from fastapi import FastAPI as BaseApp
from fastapi import APIRouter

class FastAPI(BaseApp):
    def __init__(self, container, *args, **kwargs):
        conf = {
            'title': container.config.TITLE(),
            'description': container.config.DESCRIPTION(),
            'docs_url': container.config.DOCS_URL(),
            'redoc_url': container.config.REDOCS_URL(),
            'openapi_url': container.config.OPENAPI_URL(),
        }
        super().__init__(*args, **conf, **kwargs)


class NoSchemaRouter(APIRouter):

    def get(self, *args, **kwargs):
        self.include_in_schema = False
        return self.api_route(*args, **kwargs)
