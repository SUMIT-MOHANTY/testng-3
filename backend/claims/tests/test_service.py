from decimal import Decimal
from backend.claims.dto import ClaimCreateDTO
from backend.claims.service import ClaimService
from backend.claims.errors import AmountExceeded

class DummySession:
    def __init__(self):
        self.storage = {}
    def add(self, obj):
        self.storage[obj.id] = obj
    def commit(self):
        pass
    def refresh(self, obj):
        pass
    def query(self, model):
        class Q:
            def __init__(self, storage):
                self.storage = storage
            def filter(self, *a, **kw):
                return self
            def first(self):
                return next(iter(self.storage.values()), None)
        return Q(self.storage)

def test_amount_limit():
    session = DummySession()
    svc = ClaimService(session)
    dto = ClaimCreateDTO(policy_id="p", user_id="u", amount=Decimal('60000'), documents=["d"])
    try:
        svc.submit_claim(dto, "idem")
    except AmountExceeded:
        assert True
    else:
        assert False
