from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Self

from app.domain.const import CreateSchemaType, ModelType, UpdateSchemaType
from app.domain.repository.crud import CRUDRepository


class UnitOfWork(ABC):
    def __init__(
        self,
        repository: CRUDRepository[
            ModelType,
            CreateSchemaType,
            UpdateSchemaType,
        ],
    ) -> None:
        self.repository = repository

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
