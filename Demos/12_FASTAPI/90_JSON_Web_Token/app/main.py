from fastapi import FastAPI
from app.api.routes import accounts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Banking API Demo")

app.include_router(accounts.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)