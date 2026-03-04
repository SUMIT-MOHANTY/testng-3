from sqlalchemy.orm import Session
from . import models, schemas, security
from . import models, security, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user_in: schemas.UserCreate):
    hashed = security.get_password_hash(user_in.password)
    db_user = models.User(email=user_in.email, hashed_password=hashed)
    hashed_password = security.get_password_hash(user_in.password)
    db_user = models.User(username=user_in.username, email=user_in.email, hashed_password=hashed_password)
    hashed = get_password_hash(user_in.password)
    db_user = models.User(email=user_in.email, hashed_password=hashed)
    hashed_pw = get_password_hash(user_in.password)
    db_user = models.User(email=user_in.email, hashed_password=hashed_pw)
from . import models, schemas

# ---- Users ----
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
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

def create_item(db: Session, item_in: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item_in.dict(), owner_id=user_id)
# ---- Items ----
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
def create_ledger_entry(db: Session, sender_id: int, recipient_id: int, amount):
    entry = models.LedgerEntry(sender_id=sender_id, recipient_id=recipient_id, amount=amount)
    db.add(entry)
    db.commit()
    return entry
