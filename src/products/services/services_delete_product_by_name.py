from src.products.repository.delete_product_by_name import delete_product_by_name

async def delete_product_by_name_service(name: str) -> bool:
    return await delete_product_by_name(name)
