from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def list_items():
    return [{"id": 1, "title": "Item 1"}]

@router.get('/{item_id}')
def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail='Item not found')
    return {"id": 1, "title": "Item 1"}
