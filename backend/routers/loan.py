from fastapi import APIRouter, HTTPException
import os

router = APIRouter()

LOAN_SERVICE_KEY = os.getenv('LOAN_SERVICE_KEY', 'your-key')

@router.post('/loan/originate')
async def originate_loan(amount: float, borrower: str):
    if amount <= 0:
        raise HTTPException(status_code=400, detail='Amount must be positive')
    return {
        'status': 'originated',
        'amount': amount,
        'borrower': borrower,
        'service_key': LOAN_SERVICE_KEY,
    }

@router.post('/loan/repay')
async def repay_loan(loan_id: str, amount: float):
    if amount <= 0:
        raise HTTPException(status_code=400, detail='Amount must be positive')
    return {
        'status': 'repayment_received',
        'loan_id': loan_id,
        'amount': amount,
    }

@router.get('/loan/status/{loan_id}')
async def loan_status(loan_id: str):
    # Placeholder - in real app this would query the immutable ledger
    return {'loan_id': loan_id, 'status': 'active'}
