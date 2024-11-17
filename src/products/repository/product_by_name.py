from src.config.db_mongo.db_mongo import db
from src.products.models.product_response import ProductResponseSchema
from src.products.models.format_product import format_product

async def fetch_product_by_name(name: str) -> ProductResponseSchema:
    """Busca un producto por su nombre."""
    product = await db.database["products"].find_one({"name": name})
    if product:
        return ProductResponseSchema(**format_product(product))
    return None
