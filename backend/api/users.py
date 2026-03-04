from fastapi import APIRouter, Depends, HTTPException, status
from backend.schemas.user import UserCreate, UserRead
from backend.services.user_service import create_user, get_user

router = APIRouter()

@router.post('/users', response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create(user_in: UserCreate):
    return create_user(user_in)

@router.get('/users/{user_id}', response_model=UserRead)
def read(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user
