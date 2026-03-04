from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.db import Base

class Policy(Base):
    __tablename__ = "insurance_policy"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_code = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default='ACTIVE')
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=func.now())
    premiums = relationship('Premium', back_populates='policy', cascade='all, delete-orphan')
    claims = relationship('Claim', back_populates='policy', cascade='all, delete-orphan')

class Premium(Base):
    __tablename__ = "insurance_premium"
    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('insurance_policy.id'), nullable=False)
    due_date = Column(Date, nullable=False)
    amount_cents = Column(Integer, nullable=False)
    paid = Column(Boolean, default=False)
    paid_at = Column(DateTime, nullable=True)
    policy = relationship('Policy', back_populates='premiums')

class Claim(Base):
    __tablename__ = "insurance_claim"
    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('insurance_policy.id'), nullable=False)
    claim_amount_cents = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False, default='PENDING')
    submitted_at = Column(DateTime, default=func.now())
    resolved_at = Column(DateTime, nullable=True)
    policy = relationship('Policy', back_populates='claims')
