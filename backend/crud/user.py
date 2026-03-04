from sqlalchemy.orm import Session
from .. import models, schemas
from ..security import get_password_hash

def create_user(db: Session, user_in: schemas.UserCreate):
    user = models.User(username=user_in.username,
                       email=user_in.email,
                       password_hash=get_password_hash(user_in.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def update_user(db: Session, user: models.User, data: schemas.UserUpdate):
    for field, value in data.dict(exclude_unset=True).items():
        if field == "password":
            setattr(user, "password_hash", get_password_hash(value))
        else:
            setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()

def get_role_by_name(db: Session, name: str):
    return db.query(models.Role).filter(models.Role.name == name).first()

def add_role_to_user(db: Session, user: models.User, role: models.Role):
    if role not in user.roles:
        user.roles.append(role)
        db.commit()
        db.refresh(user)
    return user
