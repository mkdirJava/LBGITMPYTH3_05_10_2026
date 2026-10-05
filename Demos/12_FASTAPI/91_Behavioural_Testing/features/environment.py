# features/environment.py
from httpx import ASGITransport
from app.main import app

def before_all(context):
    context.transport = ASGITransport(app=app)

