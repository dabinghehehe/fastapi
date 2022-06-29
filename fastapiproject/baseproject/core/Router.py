from api.Base import api_router
from views.Base import views_router
from fastapi import APIRouter


Allrouter = APIRouter()
# 视图路由
Allrouter.include_router(views_router)
# API路由
Allrouter.include_router(api_router)

