
from fastapi import APIRouter, Depends
from app.api.deps import get_settings

router = APIRouter(prefix="/info", tags=["Info"])

@router.get("/info")
def get_info(settings = Depends(get_settings)):
    return {"app_name": settings.app_name}
