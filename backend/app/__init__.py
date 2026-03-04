from fastapi import FastAPI
from .core.logger import LoggerMiddleware
from .core.error_handling import ErrorHandlingMiddleware
from .core.rate_limit import RateLimitMiddleware
from .api.router import api_router

def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(LoggerMiddleware)
    app.include_router(api_router)
    return app

app = create_app()
