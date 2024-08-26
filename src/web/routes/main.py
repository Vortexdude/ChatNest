from fastapi import APIRouter, Request
from src.web import templates

router = APIRouter()


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
