from fastapi import Depends
from backend.db.session import get_db
def get_db_dep():
    return Depends(get_db)
