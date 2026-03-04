from datetime import date
from sqlalchemy.orm import Session
from backend.models import User, Account, Loan, InsurancePolicy, Claim

def seed(session: Session):
    # Users
    user1 = User(name="Alice Example", email="alice@example.com", hashed_password="hashed", role="customer")
    user2 = User(name="Bob Admin", email="bob@example.com", hashed_password="hashed", role="admin")
    session.add_all([user1, user2])
    session.flush()
    # Accounts
    acct1 = Account(user_id=user1.id, type="checking", balance=1000.00)
    acct2 = Account(user_id=user1.id, type="savings", balance=5000.00)
    session.add_all([acct1, acct2])
    # Loans
    loan1 = Loan(user_id=user1.id, principal=20000.00, interest_rate=0.045, term_months=60, status="approved")
    session.add(loan1)
    # Insurance Policies
    pol1 = InsurancePolicy(
        user_id=user1.id,
        policy_number="POL12345",
        coverage_amount=100000.00,
        premium=120.00,
        effective_date=date.today(),
        expiry_date=date.today().replace(year=date.today().year + 1),
    )
    session.add(pol1)
    session.flush()
    # Claims
    claim1 = Claim(policy_id=pol1.id, claim_number="CLM54321", amount_requested=5000.00, status="submitted")
    session.add(claim1)
    session.commit()
