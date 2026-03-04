from fastapi import FastAPI
from .config import Settings
from .core.logger import logger

def create_app() -> FastAPI:
    settings = Settings()
    logger.info('Creating FastAPI app with settings loaded')
    app = FastAPI(title=settings.app_name)
    from .api.router import router
    app.include_router(router)
    return app
