from app.core.config import settings

def get_settings():
    return settings

def get_db():
    return "My DB Connection" # create_db_connection()

from dotenv import load_dotenv
import os

load_dotenv()

def get_api_key() -> str:
    return os.getenv("API_KEY")

