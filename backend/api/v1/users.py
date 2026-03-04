from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def list_users():
    return [{"id": 1, "name": "Alice"}]

@router.get('/{user_id}')
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail='User not found')
    return {"id": 1, "name": "Alice"}
