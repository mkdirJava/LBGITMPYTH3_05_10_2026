from fastapi import FastAPI
from fastapi import APIRouter

# app = FastAPI()
router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello World"}