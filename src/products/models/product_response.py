from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
class ProductResponseSchema(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: float
    stock: int

    class Config:
        json_encoders = {
            ObjectId: str,
        }
