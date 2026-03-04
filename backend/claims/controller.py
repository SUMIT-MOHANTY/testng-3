from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from backend.auth.security import verify_jwt
from backend.db.base import SessionLocal
from .dto import ClaimCreateDTO, ClaimValidateDTO, ClaimApproveDTO, ClaimResponseDTO, ErrorDTO
from .service import ClaimService
from .errors import ClaimNotFound, DocumentMissing, AmountExceeded, IdempotencyConflict

claims_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@claims_router.post("/claims", response_model=ClaimResponseDTO, status_code=status.HTTP_201_CREATED)
async def submit_claim(request: Request, dto: ClaimCreateDTO, db: Session = Depends(get_db), token: str = Depends(verify_jwt)):
    idem = request.headers.get("X-Idempotency-Key")
    if not idem:
        raise HTTPException(status_code=400, detail="Idempotency key required")
    service = ClaimService(db)
    try:
        claim = service.submit_claim(dto, idem)
    except AmountExceeded as e:
        raise HTTPException(status_code=400, detail=str(e))
    except IdempotencyConflict as e:
        raise HTTPException(status_code=409, detail=str(e))
    return ClaimResponseDTO(claim_id=str(claim.id), status=claim.status.value, created_at=claim.submitted_at.isoformat())

@claims_router.post("/claims/{claim_id}/validate", response_model=ClaimResponseDTO)
async def validate_claim(request: Request, claim_id: str, dto: ClaimValidateDTO, db: Session = Depends(get_db), token: str = Depends(verify_jwt)):
    idem = request.headers.get("X-Idempotency-Key")
    if not idem:
        raise HTTPException(status_code=400, detail="Idempotency key required")
    service = ClaimService(db)
    try:
        claim = service.validate_claim(claim_id, dto, idem)
    except (ClaimNotFound, DocumentMissing) as e:
        raise HTTPException(status_code=400, detail=str(e))
    return ClaimResponseDTO(claim_id=str(claim.id), status=claim.status.value, created_at=claim.submitted_at.isoformat())

@claims_router.post("/claims/{claim_id}/approve", response_model=ClaimResponseDTO)
async def approve_claim(request: Request, claim_id: str, dto: ClaimApproveDTO, db: Session = Depends(get_db), token: str = Depends(verify_jwt)):
    idem = request.headers.get("X-Idempotency-Key")
    if not idem:
        raise HTTPException(status_code=400, detail="Idempotency key required")
    service = ClaimService(db)
    try:
        claim = service.approve_claim(claim_id, dto, idem)
    except ClaimNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    return ClaimResponseDTO(claim_id=str(claim.id), status=claim.status.value, created_at=claim.submitted_at.isoformat())

@claims_router.post("/claims/{claim_id}/payout", response_model=ClaimResponseDTO)
async def payout_claim(request: Request, claim_id: str, db: Session = Depends(get_db), token: str = Depends(verify_jwt)):
    idem = request.headers.get("X-Idempotency-Key")
    if not idem:
        raise HTTPException(status_code=400, detail="Idempotency key required")
    service = ClaimService(db)
    try:
        claim = service.payout_claim(claim_id, idem)
    except ClaimNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return ClaimResponseDTO(claim_id=str(claim.id), status=claim.status.value, created_at=claim.submitted_at.isoformat())
