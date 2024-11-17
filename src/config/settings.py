from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_TITLE: str = "Product Management API"
    APP_DESCRIPTION: str = "API for managing products using FastAPI and MongoDB."
    APP_VERSION: str = "1.0.0"
    DATABASE_URI: str = "mongodb://localhost:27017"
    ALLOWED_ORIGINS: list = ["*"]

settings = Settings()
