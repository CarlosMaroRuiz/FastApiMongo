from fastapi import APIRouter, HTTPException
from src.products.models.product_response import ProductResponseSchema
from src.products.models.product import Product
from src.products.services import service_add_product,services_get_products
from src.products.services.services_get_product_by_name import get_product_by_name_service
from src.products.services.services_delete_product_by_name import delete_product_by_name_service

router = APIRouter()
@router.get("/", response_model=list[ProductResponseSchema])
async def get_all_products():
    """Devuelve una lista de todos los productos."""
    return await services_get_products.list_products()

@router.post("/", response_model=ProductResponseSchema)
async def create_new_product(product_data: Product):
    try:
        add_product = service_add_product.add_product
        product = await add_product(product_data)
        return product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/by-name/{name}", response_model=ProductResponseSchema)
async def get_product_by_name(name: str):
    product = await get_product_by_name_service(name)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/by-name/{name}")
async def delete_product_by_name(name: str):
    success = await delete_product_by_name_service(name)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": f"Product '{name}' successfully deleted"}