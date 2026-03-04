import logging
from starlette.middleware.base import BaseHTTPMiddleware
from backend.config import settings

logger = logging.getLogger('app')
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(settings.LOG_LEVEL)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def __call__(self, scope, receive, send):
        logger.info(f"Request: {scope.get('method')} {scope.get('path')}")
        return await self.app(scope, receive, send)
