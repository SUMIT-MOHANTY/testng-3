from decimal import Decimal
from backend.payments.mock_gateway import MockPaymentGateway

def execute_payout(claim_id: str, amount: Decimal, currency: str) -> dict:
    gateway = MockPaymentGateway()
    return gateway.payout(claim_id, amount, currency)
