from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .models.role import user_roles, Role

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    roles = relationship("Role", secondary=user_roles, back_populates="users")

# Placeholder for other models like Item
