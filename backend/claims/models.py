import enum
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Enum, DateTime, Numeric, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from backend.db.base import Base

class ClaimStatus(str, enum.Enum):
    SUBMITTED = "SUBMITTED"
    VALIDATED = "VALIDATED"
    APPROVED = "APPROVED"
    PAID = "PAID"
    REJECTED = "REJECTED"

class Claim(Base):
    __tablename__ = "claims"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    policy_id = Column(UUID(as_uuid=True), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    status = Column(Enum(ClaimStatus), nullable=False, default=ClaimStatus.SUBMITTED)
    amount = Column(Numeric, nullable=False)
    currency = Column(String(3), nullable=False, default="USD")
    submitted_at = Column(DateTime, default=datetime.utcnow)
    validated_at = Column(DateTime, nullable=True)
    approved_at = Column(DateTime, nullable=True)
    paid_at = Column(DateTime, nullable=True)
    idempotency_key = Column(String, unique=True, nullable=True)
