from typing import Optional
from pydantic import Field
from limberframework.config.config import BaseConfig

class DatabaseConfig(BaseConfig):
    database: Optional[str] = Field(..., env='DB_NAME')
    driver: Optional[str] = Field(..., env='DB_DRIVER')
    host: Optional[str] = Field(..., env='DB_HOST')
    path: Optional[str] = Field(..., env='DB_PATH')
    password: Optional[str] = Field(..., env='DB_PASSWORD')
    port: Optional[int] = Field(..., env='DB_PORT')
    username: Optional[str] = Field(..., env='DB_USERNAME')
