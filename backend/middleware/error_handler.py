import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def __call__(self, scope, receive, send):
        try:
            return await self.app(scope, receive, send)
        except Exception as exc:
            body = json.dumps({"detail": str(exc)})
            response = JSONResponse(content=body, status_code=500)
            await response(scope, receive, send)
