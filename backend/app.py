from fastapi import FastAPI
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI(title="Demo API")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    from .api.v1 import users, items
    app.include_router(users.router, prefix="/api/v1")
    app.include_router(items.router, prefix="/api/v1")
    return app
