from abc import ABC, abstractmethod
from typing import Any, Sequence

from pydantic import BaseModel


class CRUDRepository[
    ModelT: BaseModel,
    CreateSchemaT: BaseModel,
    UpdateSchemaT: BaseModel,
](ABC):
    @abstractmethod
    async def get_all(
        self,
    ) -> Sequence[ModelT]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(
        self,
        entity_id: Any,
    ) -> ModelT | None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, object: CreateSchemaT) -> ModelT:
        raise NotImplementedError()

    @abstractmethod
    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: UpdateSchemaT,
    ) -> ModelT:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, entity_id: Any) -> None:
        raise NotImplementedError()
