
from src.config.db_mongo.db_mongo import db
from src.products.models.product_response import ProductResponseSchema
from  src.products.models.format_product import format_product
async def fetch_all_products() -> list[ProductResponseSchema]:
    products = await db.database["products"].find().to_list(100)
    return [ProductResponseSchema(**format_product(product)) for product in products]
