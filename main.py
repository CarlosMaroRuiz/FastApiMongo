from fastapi import FastAPI
from src.routes import include_routes
from src.middlewares import add_middlewares
from src.config.settings import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

add_middlewares(app)
include_routes(app)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
