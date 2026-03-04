class ClaimNotFound(Exception):
    pass

class InvalidPolicy(Exception):
    pass

class DocumentMissing(Exception):
    pass

class AmountExceeded(Exception):
    pass

class IdempotencyConflict(Exception):
    pass
