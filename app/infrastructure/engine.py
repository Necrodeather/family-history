from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


class SqlAlchemyEngine:
    def __init__(self, uri: str, echo: bool = False) -> None:
        self._engine = create_async_engine(url=uri, echo=echo)

    def create_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            self._engine,
            expire_on_commit=False,
        )
