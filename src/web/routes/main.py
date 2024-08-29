from fastapi import APIRouter, Request
from fastapi.responses import FileResponse
from src.web import templates

router = APIRouter()

favicon_path = "src/static/svgs/favicon.svg"

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@router.get("/login")
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register")
async def home(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/chat")
async def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.get("/room")
async def home(request: Request):
    return templates.TemplateResponse("room.html", {"request": request})
