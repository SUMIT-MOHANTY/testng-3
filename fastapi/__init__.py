class Request: pass
class HTTPException(Exception):
    def __init__(self, status_code, detail=None):
        self.status_code = status_code
        self.detail = detail
class APIRouter:
    def __init__(self):
        self.routes = []
    def get(self, path):
        def deco(func):
            self.routes.append(('GET', path, func))
            return func
        return deco
    def post(self, path):
        def deco(func):
            self.routes.append(('POST', path, func))
            return func
        return deco
class FastAPI:
    def __init__(self):
        self.routes = []
        self.middleware = []
    def get(self, path):
        def deco(func):
            self.routes.append(('GET', path, func))
            return func
        return deco
    def post(self, path):
        def deco(func):
            self.routes.append(('POST', path, func))
            return func
        return deco
    def include_router(self, router):
        self.routes.extend(router.routes)
    def add_middleware(self, middleware_cls, **kw):
        self.middleware.append((middleware_cls, kw))
