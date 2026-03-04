# Insurance Module

This module implements basic insurance policy management:
- Policy creation (restricted to role `insurer`)
- Automatic premium scheduling & daily deduction job (`run_premium_schedule`)
- Claim filing by policy owners
- All mutating actions are recorded in the Confidential Ledger via `backend.audit.ledger.record_entry`.

Key files:
- `models.py`: SQLAlchemy ORM definitions.
- `schemas.py`: Pydantic request/response models.
- `router.py`: FastAPI endpoints.
- `jobs.py`: Background premium deduction logic.
- `utils.py`: Stubs for external provider validation and debit operations.

Environment:
- Ensure `.env` contains `INSURANCE_API_KEY`.

Testing:
- Run `pytest backend/insurance/tests/` to execute the lifecycle tests.
