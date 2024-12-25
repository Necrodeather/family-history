from abc import ABC, abstractmethod
from typing import Type
from uuid import UUID

from pydantic import BaseModel

from app.domain.entities.base import BaseEntity
from app.domain.uow import UnitOfWork


class CRUDService[
    CreateSchemaT: BaseModel,
    UpdateSchemaT: BaseModel,
    ReadSchemaT: BaseModel,
](ABC):
    def __init__(
        self,
        uow: UnitOfWork,
        read_entity: Type[BaseEntity],
    ) -> None:
        self._read_entity = read_entity
        self._uow = uow

    @abstractmethod
    async def get_all(self) -> list[ReadSchemaT]:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, entity_id: UUID) -> ReadSchemaT:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: CreateSchemaT) -> ReadSchemaT:
        raise NotImplementedError()

    @abstractmethod
    async def update_by_id(
        self,
        entity_id: UUID,
        entity: UpdateSchemaT,
    ) -> ReadSchemaT:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, entity_id: UUID) -> None:
        raise NotImplementedError()
