import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 5, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window = window_seconds
        self.clients: dict[str, list[float]] = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "anonymous"
        now = time.time()
        timestamps = self.clients.get(client_ip, [])
        timestamps = [t for t in timestamps if now - t < self.window]
        if len(timestamps) >= self.max_requests:
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
        timestamps.append(now)
        self.clients[client_ip] = timestamps
        return await call_next(request)
