from importlib import import_module
from os import getcwd
from fastapi.middleware.cors import CORSMiddleware
from limberframework.database.middleware import DatabaseSessionMiddleware
from limberframework.database.models import Model
from limberframework.foundation.application import Application
from limberframework.routing.middleware import ThrottleRequestMiddleware
from limber.config.app import AppConfig, auth, cors, models, service_providers
from limber.config.cache import CacheConfig
from limber.config.database import DatabaseConfig
from limber.routes.api import router as api_router

# Establish application
app = Application(
    base_path=getcwd() + '/' + AppConfig().name + '/storage/cache'
)

# Register services
for service_provider in service_providers:
    class_separator = service_provider.rindex('.')
    service_provider_package = service_provider[:class_separator]
    service_provider_class = service_provider[class_separator + 1:]

    service_provider = getattr(import_module(service_provider_package), service_provider_class)
    app.register(service_provider(app))

# Load configurations
app['config']['app'] = AppConfig().dict()
app['config']['auth'] = auth
app['config']['cache'] = CacheConfig().dict()
app['config']['cors'] = cors
app['config']['database'] = DatabaseConfig().dict()

# Register models
for model in models:
    import_module(model)

# Uncomment to create tables in the database from Models
# Model.metadata.create_all(bind=app['db.connection'].engine)

# Register middlewares
app.add_middleware(ThrottleRequestMiddleware, max_hits=60)
app.add_middleware(
    CORSMiddleware,
    allow_origins=app['config']['cors']['origins'],
    allow_credentials=app['config']['cors']['credentials'],
    allow_methods=app['config']['cors']['methods'],
    allow_headers=app['config']['cors']['headers']
)
app.add_middleware(DatabaseSessionMiddleware)

# Register routes
app.include_router(api_router)
