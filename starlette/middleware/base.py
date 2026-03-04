class BaseHTTPMiddleware:
    def __init__(self, app, **kwargs):
        self.app = app
    async def __call__(self, scope, receive, send):
        return await self.app(scope, receive, send)
