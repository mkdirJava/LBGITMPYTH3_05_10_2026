from fastapi import FastAPI

from my_web_app.exception_handlers import apply_exception
from my_web_app.router import router as my_router 
from my_web_app.router import account_router 
app = FastAPI()
apply_exception(app)
app.include_router(my_router)
app.include_router(account_router)

