from src.products.repository.create_product import create_product
from src.products.models.product import Product

async def add_product(product_data: Product) -> dict:
    """Crea un producto en la base de datos y devuelve sus datos."""
    return await create_product(product_data)
