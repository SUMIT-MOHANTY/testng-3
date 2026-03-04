import os
from dotenv import load_dotenv
load_dotenv()

def get_insurance_api_key():
    return os.getenv("INSURANCE_API_KEY")

def validate_product_code(product_code: str) -> bool:
    # mock validation - accept any non‑empty code
    return bool(product_code)

def debit_user(user_id: int, amount_cents: int) -> bool:
    # stub - always succeeds
    return True
