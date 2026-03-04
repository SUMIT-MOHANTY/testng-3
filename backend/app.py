from fastapi import FastAPI
from .config import settings
from .database import engine
from .models import Base

def create_app() -> FastAPI:
    app = FastAPI(title="Financial Service API", version="0.1.0")
    # Create tables on startup if they do not exist
    @app.on_event("startup")
    def on_startup():
        Base.metadata.create_all(bind=engine)
    return app

app = create_app()
