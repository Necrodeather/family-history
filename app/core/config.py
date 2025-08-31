from typing import TypeVar

from pydantic import ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar('TSettings', bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


class DatabaseSettings(BaseSettings):
    """Pydantic model for database settings.

    This model contains the configuration for connecting to a PostgreSQL
    database using SQLAlchemy.

    :param driver: The driver to use when connecting to the database.
    :type driver: str
    :param user: The username to use when connecting to the database.
    :type user: str
    :param password: The password to use when connecting to the database.
    :type password: str
    :param host: The hostname of the database server.
    :type host: str, optional
    :param port: The port number of the database server.
    :type port: int, optional
    :param db: The name of the database to connect to.
    :type db: str
    :param echo: Whether to enable logging of SQL statements.
    :type echo: bool, optional
    :param uri: The connection URI for connecting to the database.
    :type uri: str, optional
    """

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
    uri: str = ''

    @field_validator('uri')
    @classmethod
    def get_uri(cls, value: str, values: ValidationInfo) -> str:
        """Generates a connection URI for connecting to the database.

        :param value: The current value of the `uri` field. If provided, it
        will be returned as-is.
        :type value: str
        :param values: A dictionary containing the values of all
        fields in the model.
        :type values: ValidationInfo
        :returns: The connection URI for connecting to the database.
        :rtype: str
        """
        if value:
            return value
        driver = values.data['driver']
        user = values.data['user']
        password = values.data['password']
        host = values.data['host']
        port = values.data['port']
        db = values.data['db']
        return f'{driver}://{user}:{password}@{host}:{port}/{db}'


class AppSettings(BaseSettings):
    """Pydantic model for application settings.

    This model contains the configuration for running a web application using
    FastAPI and Uvicorn.

    :param host: The hostname to bind the server to.
    :type host: str, optional
    :param port: The port number to listen on. Defaults to 8000.
    :type port: int, optional
    :param secret_key: A secret key used for generating JWT tokens.
    :type secret_key: str
    :param debug_reload: Whether to enable Uvicorn's debug and
    auto-reload features.
    :type debug_reload: bool, optional
    :param workers: The number of worker processes to use with
    Uvicorn.
    :type workers: int, optional
    :param refresh_token_expire_minutes: The number of minutes
    until a refresh token expires.
    :type refresh_token_expire_minutes: int, optional
    :param access_token_expire_minutes: The number of minutes
    until an access token expires.
    :type access_token_expire_minutes: int, optional
    :param algorithm: The JWT encoding algorithm to use.
    :type algorithm: str, optional
    """

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
    """Pydantic model for Redis settings.

    This model contains the configuration for connecting to a Redis instance.

    :param host: The hostname of the Redis server.
    :type host: str, optional
    :param port: The port number of the Redis server.
    :type port: int, optional
    :param db: The database index to use when connecting to Redis.
    :type db: int, optional
    :param uri: The connection URI for connecting to Redis.
    :type uri: str, optional
    """

    model_config = SettingsConfigDict(
        env_file='./.env',
        env_prefix='redis_',
        extra='ignore',
    )

    host: str = 'localhost'
    port: int = 6379
    db: int = 0
    uri: str = ''

    @field_validator('uri')
    @classmethod
    def get_uri(cls, value: str, values: ValidationInfo) -> str:
        """Generates a connection URI for connecting to Redis.

        :param value: The current value of the `uri` field. If provided,
        it will be returned as-is.
        :type value: str
        :param values: A dictionary containing the values of
        all fields in the model.
        :type values: ValidationInfo
        :returns: The connection URI for connecting to Redis.
        :rtype: str
        """
        if value:
            return value
        host = values.data['host']
        port = values.data['port']
        db = values.data['db']
        return f'redis://{host}:{port}/{db}'


database_settings: DatabaseSettings = get_settings(DatabaseSettings)
app_settings: AppSettings = get_settings(AppSettings)
redis_settings: RedisSettings = get_settings(RedisSettings)
