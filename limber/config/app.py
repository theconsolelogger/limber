from typing import Optional
from pydantic import Field
from limberframework.config.config import BaseConfig

auth = {
    'driver': 'apikey'
}

cors = {
    'origins': [],
    'credentials': False,
    'methods': [],
    'headers': []
}

models = [
    'limber.app.models.user'
]

service_providers = [
    'limberframework.authentication.authentication_service_provider.AuthServiceProvider',
    'limberframework.cache.cache_service_provider.CacheServiceProvider',
    'limberframework.config.config_service_provider.ConfigServiceProvider',
    'limberframework.database.database_service_provider.DatabaseServiceProvider',
]

class AppConfig(BaseConfig):
    name: Optional[str] = Field(..., env='APP_NAME')
