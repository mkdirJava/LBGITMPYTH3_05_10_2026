from fastapi import FastAPI
from app.api.routes import items, root
app = FastAPI()
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(root.router, prefix="/root", tags=["Root"])
