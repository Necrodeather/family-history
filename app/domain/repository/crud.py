from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence

from app.domain.types import CreateSchemaType, ModelType, UpdateSchemaType


class CRUDRepository(
    ABC,
    Generic[
        ModelType,
        CreateSchemaType,
        UpdateSchemaType,
    ],
):
    @abstractmethod
    async def get_all(
        self,
    ) -> Sequence[ModelType]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(
        self,
        entity_id: Any,
    ) -> ModelType | None:
        raise NotImplementedError

    @abstractmethod
    async def create(self, object: CreateSchemaType) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: UpdateSchemaType,
    ) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, entity_id: Any) -> None:
        raise NotImplementedError
