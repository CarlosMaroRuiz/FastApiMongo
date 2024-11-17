from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import  settings

def add_middleware_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
