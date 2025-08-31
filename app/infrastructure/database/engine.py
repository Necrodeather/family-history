from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


class SqlAlchemyEngine:
    """A wrapper around the SQLAlchemy async engine and session factory."""

    def __init__(self, uri: str, echo: bool = False) -> None:
        """Initializes the engine.

        :param uri: The database URI.
        :type uri: str
        :param echo: Whether to echo SQL statements.
        :type echo: bool
        """
        self._engine = create_async_engine(url=uri, echo=echo)
        self._session_factory = async_sessionmaker(
            self._engine,
            expire_on_commit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """Provides a session to interact with the database.

        :returns: An async session.
        :rtype: AsyncGenerator[AsyncSession, None]
        """
        async with self._session_factory() as session:
            yield session
