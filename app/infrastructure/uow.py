from typing import Any, AsyncGenerator, Self, Type

from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from app.core.config import database_settings
from app.domain.uow import UnitOfWork
from app.infrastructure.engine import SqlAlchemyEngine
from app.infrastructure.repository.base import SQLAlchemyCRUDRepository


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, repository: Type[SQLAlchemyCRUDRepository]) -> None:
        self.engine = SqlAlchemyEngine(
            uri=database_settings.uri,
            echo=database_settings.echo,
        )
        self.repository = repository
        self.session: AsyncSession

    async def __aenter__(self) -> Self:
        self.session = self.engine.create_session_maker()
        self.repository = self.repository(self.session)
        return self

    async def __aexit__(self, *args: list[Any]) -> None:
        await self.commit()
        await self.session.close()

    async def begin(
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
