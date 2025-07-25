from typing import TypeVar

from pydantic import ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar('TSettings', bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_prefix='postgres_',
        extra='ignore',
    )

    driver: str = 'postgresql+asyncpg'
    user: str
    password: str
    host: str = 'localhost'
    port: int = 5432
    db: str
    echo: bool = False
    uri: str = ""

    @field_validator("uri")
    @classmethod
    def get_uri(cls, value: str, values: ValidationInfo) -> str:
        if value:
            return value
        driver = values.data["driver"]
        user = values.data["user"]
        password = values.data["password"]
        host = values.data["host"]
        port = values.data["port"]
        db = values.data["db"]
        return f'{driver}://{user}:{password}@{host}:{port}/{db}'


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_prefix='app_',
        extra='ignore',
    )
    host: str = 'localhost'
    port: int = 8000
    secret_key: str
    debug_reload: bool = False
    workers: int = 1
    refresh_token_expire_minutes: int = 15
    access_token_expire_minutes: int = 5
    algorithm: str = 'HS256'


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_prefix='redis_',
        extra='ignore',
    )

    host: str = 'localhost'
    port: int = 6379
    db: int = 0


database_settings: DatabaseSettings = get_settings(DatabaseSettings)
app_settings: AppSettings = get_settings(AppSettings)
redis_settings: RedisSettings = get_settings(RedisSettings)
