class BaseModel:
    def dict(self, *a, **k):
        return self.__dict__
def Field(default=None, **kw):
    return default
