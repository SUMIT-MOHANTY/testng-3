from datetime import datetime
from sqlalchemy import Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

class Claim(Base):
    __tablename__ = "claims"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    policy_id: Mapped[int] = mapped_column(ForeignKey("insurance_policies.id"), nullable=False)
    claim_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    amount_requested: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="submitted")
    filed_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    policy: Mapped["InsurancePolicy"] = relationship("InsurancePolicy")
