from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import users, items

def create_app() -> FastAPI:
    app = FastAPI(title="Sample FastAPI Project")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(users.router)
    app.include_router(items.router)
    return app

app = create_app()
