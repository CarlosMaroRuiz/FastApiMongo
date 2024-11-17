from motor.motor_asyncio import AsyncIOMotorClient
from src.config.settings import settings

client = AsyncIOMotorClient(settings.DATABASE_URI)
db = client["product_management"]
