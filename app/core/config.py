from typing import TypeVar
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)


def get_settings(cls: type[TSettings]) -> TSettings:
    return cls()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="~/.env",
        env_prefix="postgres_",
        extra="ignore",
    )

    driver: str = "postgresql+asyncpg"
    user: str
    password: str
    host: str = "localhost"
    port: int = 5432
    db: str

    @property
    def uri(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


database_settings: DatabaseSettings = get_settings(DatabaseSettings)
