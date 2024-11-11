from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, TypeVar

ModelType = TypeVar('ModelType')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


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
    async def remove_by_id(self, entity_id: Any) -> None:
        raise NotImplementedError
