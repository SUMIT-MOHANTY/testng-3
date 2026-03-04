from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

# Configure logger: console + file (development)
logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add("app.log", rotation="10 MB", level="DEBUG")

class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response: Response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response
