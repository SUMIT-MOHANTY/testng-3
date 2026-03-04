from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/transfer", response_model=schemas.TransferResponse)
def transfer_funds(request: schemas.TransferRequest,
                   db: Session = Depends(dependencies.get_db),
                   current_user: models.User = Depends(dependencies.get_current_user)):
    recipient = crud.get_user(db, request.recipient_id)
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    if current_user.balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    # Debit sender
    crud.update_balance(db, current_user, -request.amount)
    # Credit recipient
    crud.update_balance(db, recipient, request.amount)
    # Ledger
    crud.create_ledger_entry(db, current_user.id, recipient.id, request.amount)
    return schemas.TransferResponse(success=True, new_balance=current_user.balance)
