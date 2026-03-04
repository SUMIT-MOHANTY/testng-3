from fastapi import APIRouter
from ..config import settings
from ..schemas.config_schema import ConfigResponse

router = APIRouter()

@router.get("/config", response_model=ConfigResponse)
async def get_config():
    return ConfigResponse(LOG_ENDPOINT=settings.LOG_ENDPOINT)
