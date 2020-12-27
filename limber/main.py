from importlib import import_module
from os.path import abspath
from fastapi.middleware.cors import CORSMiddleware
from limberframework.config.config_service_provider import ConfigServiceProvider
from limberframework.database.middleware import DatabaseSessionMiddleware
from limberframework.database.models import Model
from limberframework.foundation.application import Application
from limberframework.routing.middleware import ThrottleRequestMiddleware
from limber.routes.api import router as api_router
import logging

logger = logging.getLogger()
logger.setLevel('DEBUG')

# Establish application
app = Application(
    base_path=abspath("limber")
)

@app.on_event("startup")
async def startup():
    # Load configurations
    config_service_provider = ConfigServiceProvider()
    config_service_provider.register(app)
    config_service = await app.make('config')

    # Register services
    service_providers = config_service.get_section('service providers')

    for service_provider in service_providers:
        service_provider_class = getattr(import_module(service_providers[service_provider]), service_provider)
        service_provider_class().register(app)

    # Load services
    await app.load_services()

    # Register models
    models = config_service.get_section('models')

    for model in models:
        import_module(models[model])

    # Uncomment to create tables in the database from Models
    # Model.metadata.create_all(bind=app['db.connection'].engine)

    # Register middlewares
    app.add_middleware(ThrottleRequestMiddleware, max_hits=60)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config_service.get_section('cors.origins'),
        allow_credentials=config_service['cors'].getboolean('credentials'),
        allow_methods=config_service.get_section('cors.methods'),
        allow_headers=config_service.get_section('cors.headers')
    )
    app.add_middleware(DatabaseSessionMiddleware)

    # Register routes
    app.include_router(api_router)
