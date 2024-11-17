from src.products.repository.product_by_name import fetch_product_by_name

async def get_product_by_name_service(name: str):
    """Lógica del servicio para buscar un producto por nombre."""
    product = await fetch_product_by_name(name)
    if not product:
        return None
    return product
