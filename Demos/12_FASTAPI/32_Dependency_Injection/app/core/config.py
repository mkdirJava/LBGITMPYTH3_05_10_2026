from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Banking API"

settings = Settings()