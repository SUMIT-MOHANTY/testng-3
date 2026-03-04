class FastAPI:
    def __init__(self, title='FastAPI'): pass
    def add_middleware(self, mw, **opt): pass
    def include_router(self, router, prefix=''): pass

class APIRouter:
    def __init__(self): pass
    def get(self, path):
        def deco(fn): return fn
        return deco
    def post(self, path):
        def deco(fn): return fn
        return deco

def Depends(dep):
    return None

class HTTPException(Exception):
    def __init__(self, status_code, detail=None):
        self.status_code = status_code
        self.detail = detail
