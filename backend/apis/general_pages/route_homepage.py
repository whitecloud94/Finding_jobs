#route_homepage.py


from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

general_pages_router = APIRouter()
templates = Jinja2Templates(directory="templates")



@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})
	