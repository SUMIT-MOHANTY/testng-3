from datetime import date
from sqlalchemy import Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    policy_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    coverage_amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    premium: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    effective_date: Mapped[date] = mapped_column(Date, nullable=False)
    expiry_date: Mapped[date] = mapped_column(Date, nullable=False)
    holder: Mapped["User"] = relationship("User")
