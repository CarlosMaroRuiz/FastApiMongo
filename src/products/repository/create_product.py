
from src.config.db_mongo.db_mongo import db
from src.products.models.product import Product
from  src.products.models.format_product import format_product


async def create_product(product: Product) -> dict:
    """Inserta un producto en la base de datos y devuelve sus datos."""
    result = await db.database["products"].insert_one(product.dict())
    created_product = await db.database["products"].find_one({"_id": result.inserted_id})
    return format_product(created_product)


