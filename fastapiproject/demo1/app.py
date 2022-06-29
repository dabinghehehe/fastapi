from fastapi import FastAPI
from api.Base import router
from config import settings

application = FastAPI(
    debug=settings.APP_DEBUG,
    # docs_url=None,
    # redoc_url=None
    )

application.include_router(router)

app = application