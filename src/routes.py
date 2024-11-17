from fastapi import FastAPI
from src.products.router import  router as products_router
#funcion para incluir rutas
def include_routes(app: FastAPI):
    app.include_router(products_router, prefix="/products", tags=["Products"])
