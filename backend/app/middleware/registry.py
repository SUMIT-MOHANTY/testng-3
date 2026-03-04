from fastapi import FastAPI
from .logging import LoggingMiddleware
from .error_handling import ErrorHandlingMiddleware
from .rate_limit import RateLimitMiddleware, limiter
from slowapi import _rate_limit_exceeded_handler

def register_middleware(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.state.limiter = limiter
    app.add_exception_handler(429, _rate_limit_exceeded_handler)
