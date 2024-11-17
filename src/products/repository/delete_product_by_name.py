from src.config.db_mongo.db_mongo import db

async def delete_product_by_name(name: str) -> bool:
    """
    Elimina un producto por su nombre.

    Args:
        name (str): Nombre del producto.

    Returns:
        bool: True si se eliminó un documento, False de lo contrario.
    """
    result = await db.database["products"].delete_one({"name": name})
    return result.deleted_count > 0  # True si se elimino un documento
