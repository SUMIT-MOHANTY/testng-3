from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.models import Base

class Policy(Base):
    __tablename__ = "policies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_code: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="ACTIVE")
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    premiums = relationship("Premium", back_populates="policy", cascade="all, delete-orphan")
    claims = relationship("Claim", back_populates="policy", cascade="all, delete-orphan")

class Premium(Base):
    __tablename__ = "premiums"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    policy_id: Mapped[int] = mapped_column(ForeignKey("policies.id"), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    policy = relationship("Policy", back_populates="premiums")

class Claim(Base):
    __tablename__ = "claims"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    policy_id: Mapped[int] = mapped_column(ForeignKey("policies.id"), nullable=False)
    claim_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    amount_requested: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    approved: Mapped[bool] = mapped_column(Boolean, default=False)
    payout_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=True)
    policy = relationship("Policy", back_populates="claims")
