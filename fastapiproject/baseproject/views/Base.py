from fastapi import APIRouter
from starlette.responses import HTMLResponse

from views.home import home, reg_page, reg_result_page


views_router = APIRouter()


views_router.get("/items/", response_class=HTMLResponse)(home)
views_router.get("/reg", response_class=HTMLResponse)(reg_page)
views_router.post("/reg/form", response_class=HTMLResponse)(reg_result_page)


# async def read_item():
