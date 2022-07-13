from fastapi import APIRouter
from app.apis.v1.endpoints import feeds
from app.schemas.healthcheck import Healthcheck

v1_router = APIRouter()


@v1_router.get("/health_check", response_model=Healthcheck)
async def healthcheck():
    return {"is_ok": True}


v1_router.include_router(feeds.router, tags=["feeds"], prefix="/feeds")
