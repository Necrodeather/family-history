from typing import Any, AsyncGenerator, Self

from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from app.core.config import database_settings
from app.domain.types import CreateSchemaType, ModelType, UpdateSchemaType
from app.domain.uow import UnitOfWork
from app.infrastructure.database.engine import SqlAlchemyEngine
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(
        self,
        repository: SQLAlchemyCRUDRepository[
            ModelType,
            CreateSchemaType,
            UpdateSchemaType,
        ],
    ) -> None:
        self.engine = SqlAlchemyEngine(
            uri=database_settings.uri,
            echo=database_settings.echo,
        )
        self.repository_cls = repository
        self.session: AsyncSession
        self.repository: SQLAlchemyCRUDRepository  # type: ignore[type-arg]

    async def __aenter__(self) -> Self:
        self.session = self.engine.create_session_maker()()
        self.repository = self.repository_cls(self.session)
        return self

    async def __aexit__(self, *args: list[Any]) -> None:
        await self.commit()
        await self.session.close()

    async def begin(  # type: ignore[override]
        self,
    ) -> AsyncGenerator[AsyncSessionTransaction, None]:
        async with self.session.begin():
            yield

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except Exception as error:
            await self.rollback()
            raise error

    async def rollback(self) -> None:
        await self.session.rollback()
