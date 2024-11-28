from typing import Generic, Type
from uuid import UUID

from app.domain.entities.base import BaseEntity
from app.domain.types import (
    CreateSchemaType,
    ReadSchemaType,
    UpdateSchemaType,
)
from app.domain.uow import UnitOfWork


class BaseService(Generic[CreateSchemaType, UpdateSchemaType, ReadSchemaType]):
    def __init__(
        self,
        uow: UnitOfWork,
        read_entity: Type[BaseEntity],
    ) -> None:
        self._read_entity = read_entity
        self._uow = uow

    async def get_all(self) -> list[ReadSchemaType]:
        async with self._uow as uow:
            result = await uow.repository.get_all()
        return self._read_entity.from_list(result)

    async def get_by_id(self, entity_id: UUID) -> ReadSchemaType:
        async with self._uow as uow:
            result = await uow.repository.get_by_id(entity_id)
        return self._read_entity.model_validate(result)

    async def create(self, entity: CreateSchemaType) -> ReadSchemaType:
        async with self._uow as uow:
            result = await uow.repository.create(entity)
        return self._read_entity.model_validate(result)

    async def update_by_id(
        self,
        entity_id: UUID,
        entity: UpdateSchemaType,
    ) -> ReadSchemaType:
        async with self._uow as uow:
            result = await uow.repository.update_by_id(entity_id, entity)
        return self._read_entity.model_validate(result)

    async def delete_by_id(self, entity_id: UUID) -> None:
        async with self._uow as uow:
            await uow.repository.delete_by_id(entity_id)
