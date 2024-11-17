from src.products.repository.get_all_products import fetch_all_products
async def list_products() -> list:
    return await fetch_all_products()
