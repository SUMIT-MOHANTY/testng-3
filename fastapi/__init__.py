class FastAPI:
    def __init__(self, title="app"):
        self.routes = []
    def get(self, path):
        def decorator(func):
            self.routes.append(('GET', path, func))
            return func
        return decorator
    def post(self, path):
        def decorator(func):
            self.routes.append(('POST', path, func))
            return func
        return decorator
    def include_router(self, router, prefix=""):
        for method, p, fn in router.routes:
            self.routes.append((method, prefix + p, fn))

class APIRouter:
    def __init__(self):
        self.routes = []
    def get(self, path):
        def decorator(func):
            self.routes.append(('GET', path, func))
            return func
        return decorator
    def post(self, path):
        def decorator(func):
            self.routes.append(('POST', path, func))
            return func
        return decorator

def Depends(dep):
    return dep

class HTTPException(Exception):
    def __init__(self, status_code, detail=None):
        self.status_code = status_code
        self.detail = detail

class status:
    HTTP_401_UNAUTHORIZED = 401
    HTTP_404_NOT_FOUND = 404
    HTTP_200_OK = 200
