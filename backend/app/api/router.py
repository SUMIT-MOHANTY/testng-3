from fastapi import APIRouter
from .health import router as health_router
from .config import router as config_router

router = APIRouter()
router.include_router(health_router)
router.include_router(config_router)
