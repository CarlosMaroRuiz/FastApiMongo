from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

