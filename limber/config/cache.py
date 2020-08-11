from typing import Optional
from pydantic import Field
from limberframework.config.config import BaseConfig

class CacheConfig(BaseConfig):
    driver: Optional[str] = Field(..., env='CACHE_DRIVER')
    path: Optional[str] = Field('storage/cache', env='CACHE_PATH')
