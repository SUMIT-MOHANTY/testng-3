from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
