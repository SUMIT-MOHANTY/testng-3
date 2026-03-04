from sqlalchemy.orm import Session
from . import models, security, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user_in: schemas.UserCreate):
    hashed_password = security.get_password_hash(user_in.password)
    db_user = models.User(username=user_in.username, email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
