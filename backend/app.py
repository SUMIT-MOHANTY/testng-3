from fastapi import FastAPI
from .api.v1 import transfer

def create_app() -> FastAPI:
    app = FastAPI(title="Secure Fund Transfer API")
    app.include_router(transfer.router, prefix="/api/v1")
    return app

app = create_app()
