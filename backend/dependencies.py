from .database import get_db
from .security import verify_password, get_password_hash, create_access_token
from .models import User
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from .config import settings

def get_current_user(token: str = Depends(lambda: None)):
    # Simplified placeholder: in real code extract token from header
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

from .dependencies.rbac import require_role
