from .users.routes import bp as user_routes
from .providers.routes import bp as provider_routes
from .services.routes import bp as service_routes
from .user_services.routes import bp as user_service_routes

def init_app(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(provider_routes)
    app.register_blueprint(service_routes)
    app.register_blueprint(user_service_routes)
