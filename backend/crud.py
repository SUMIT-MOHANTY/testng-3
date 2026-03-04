from sqlalchemy.orm import Session
from . import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def update_balance(db: Session, user: models.User, amount):
    user.balance += amount
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.balance

def create_ledger_entry(db: Session, sender_id: int, recipient_id: int, amount):
    entry = models.LedgerEntry(sender_id=sender_id, recipient_id=recipient_id, amount=amount)
    db.add(entry)
    db.commit()
    return entry
