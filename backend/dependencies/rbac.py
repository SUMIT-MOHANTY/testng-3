from fastapi import Depends, HTTPException, status
from . import get_current_user

def require_role(*allowed_roles: str):
    def role_checker(current_user = Depends(get_current_user)):
        user_roles = {role.name for role in getattr(current_user, "roles", [])}
        if not user_roles.intersection(set(allowed_roles)):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Insufficient role")
        return current_user
    return role_checker
