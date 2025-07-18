from typing import TypeVar

from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar('TSettings', bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='~/.env',
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

    @property
    def uri(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='~/.env',
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


database_settings: DatabaseSettings = get_settings(DatabaseSettings)
app_settings: AppSettings = get_settings(AppSettings)
