from fastapi import APIRouter

route = APIRouter()


@route.get("/")
def greet():
    return {"Status": "done"}
