from fastapi import APIRouter
from .ledger import router as ledger_router

router = APIRouter()
router.include_router(ledger_router, prefix='/ledger', tags=['ledger'])
