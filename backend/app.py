from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .api.v1 import users, items, ledger

def create_app() -> FastAPI:
    app = FastAPI(title="Immutable Ledger Service", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(users.router, prefix="/api/v1", tags=["users"])
    app.include_router(items.router, prefix="/api/v1", tags=["items"])
    app.include_router(ledger.router, prefix="/api/v1", tags=["ledger"])
    return app

app = create_app()
