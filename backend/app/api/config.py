from fastapi import APIRouter
from ..config import Settings
from ..schemas.config_schema import ConfigResponse

router = APIRouter()

@router.get("/config", response_model=ConfigResponse, tags=["config"])
def get_config():
    settings = Settings()
    return ConfigResponse(app_name=settings.app_name, key_vault_url=settings.key_vault_url)
