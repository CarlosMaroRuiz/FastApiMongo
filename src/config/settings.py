from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    APP_TITLE: str = Field(default="Product Management API", env="APP_TITLE")
    APP_DESCRIPTION: str = Field(default="API for managing products using FastAPI and MongoDB.", env="APP_DESCRIPTION")
    APP_VERSION: str = Field(default="1.0.0", env="APP_VERSION")
    DATABASE_URI: str = Field(default="mongodb://localhost:27017", env="DATABASE_URI")
    ALLOWED_ORIGINS: list = Field(default=["*"], env="ALLOWED_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print(settings.DATABASE_URI)  # "mongodb://localhost:27017