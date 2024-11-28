from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Self

from app.domain.repository.crud import CRUDRepository
from app.domain.types import CreateSchemaType, ModelType, UpdateSchemaType


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
