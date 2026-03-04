from fastapi import FastAPI
from backend.middleware.logging import LoggingMiddleware
from backend.middleware.error_handler import ErrorHandlerMiddleware
from backend.middleware.rate_limit import RateLimitMiddleware
from backend.api.v1 import users, items

def create_app() -> FastAPI:
    app = FastAPI(title='Demo API')
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(ErrorHandlerMiddleware)
    app.add_middleware(RateLimitMiddleware, calls=10, period=60)
    app.include_router(users.router, prefix='/api/v1/users')
    app.include_router(items.router, prefix='/api/v1/items')
    return app
