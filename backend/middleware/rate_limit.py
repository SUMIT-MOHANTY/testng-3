import time
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, calls: int = 5, period: int = 60):
        super().__init__(app)
        self.calls = calls
        self.period = period
        self.history = {}

    async def __call__(self, scope, receive, send):
        client = scope.get('client')[0] if scope.get('client') else 'anonymous'
        now = time.time()
        timestamps = self.history.get(client, [])
        timestamps = [t for t in timestamps if now - t < self.period]
        if len(timestamps) >= self.calls:
            raise Exception('Rate limit exceeded')
        timestamps.append(now)
        self.history[client] = timestamps
        return await self.app(scope, receive, send)
