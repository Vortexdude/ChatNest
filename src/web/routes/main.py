from src.config import settings
from fastapi import Request
from fastapi.responses import FileResponse
from src.web import templates
from src.api.utils import NoSchemaRouter

router = NoSchemaRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get('/favicon.ico')
async def favicon():
    return FileResponse(settings.FAVICON_PATH)

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
