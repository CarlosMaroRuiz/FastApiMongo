from src.middlewares import middleware_cors

def add_middlewares(app):
    middleware_cors.add_middleware_cors(app)