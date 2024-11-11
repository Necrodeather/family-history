from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Self


class UnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError()

    @abstractmethod
    async def __aexit__(self, *args: list[Any]) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def begin(self) -> AsyncGenerator[Any, None]:
        raise NotImplementedError()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError()
