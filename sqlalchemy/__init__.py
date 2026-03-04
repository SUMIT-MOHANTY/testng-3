def create_engine(url):
    return None

class Column:
    def __init__(self, _type, primary_key=False, nullable=True, unique=False):
        pass

class Integer:
    pass

class String:
    def __init__(self, length=None):
        pass

def declarative_base():
    class Base:
        pass
    return Base

def sessionmaker(bind=None):
    class Session:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            pass
        def add(self, obj):
            pass
        def commit(self):
            pass
        def query(self, model):
            return []
    return Session
