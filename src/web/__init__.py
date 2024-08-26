from fastapi.templating import Jinja2Templates
from src.config import settings

templates = Jinja2Templates(directory=settings.template_dir)

