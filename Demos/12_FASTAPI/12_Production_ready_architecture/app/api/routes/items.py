from fastapi import APIRouter, HTTPException

# router = APIRouter(prefix="/items", tags=["Items"])
router = APIRouter( tags=["Items"])

@router.get("/")
def list_items():
    return []

@router.get("/{account_id}")
def get_item(account_id: int):
    if account_id != 1:
        raise HTTPException(status_code=404, detail="Not found")
    return {"account_id": account_id}

from fastapi import Depends
from app.api.deps import get_db

@router.get("/db/")
def get_items(db=Depends(get_db)):
    return {"db": db}
