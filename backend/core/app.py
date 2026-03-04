from fastapi import FastAPI
from .config import Settings
from backend.api.users import router as users_router

def create_app() -> FastAPI:
    app = FastAPI(title='Financial Service API')
    app.include_router(users_router, prefix='/api/v1')
    return app
