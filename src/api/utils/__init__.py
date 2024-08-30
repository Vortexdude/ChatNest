from fastapi import APIRouter


class NoSchemaRouter(APIRouter):

    def get(self, *args, **kwargs):
        self.include_in_schema = False
        return self.api_route(*args, **kwargs)
