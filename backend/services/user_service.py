from backend.models.user import User, Base
from backend.db.session import get_db
from backend.schemas.user import UserCreate
from sqlalchemy.orm import Session
def _hash_pwd(pwd: str) -> str:
    return pwd  # placeholder - replace with real hashing
def create_user(user_in: UserCreate) -> User:
    db: Session = next(get_db())
    db_user = User(email=user_in.email, full_name=user_in.full_name, hashed_password=_hash_pwd(user_in.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_user(user_id: int) -> User | None:
    db: Session = next(get_db())
    return db.query(User).filter(User.id == user_id).first()
