from typing import Type
from uuid import UUID

from pydantic import BaseModel

from app.domain.entities.queries import BaseQuery
from app.domain.exceptions import NotFoundError
from app.infrastructure.database.base import Base
from app.infrastructure.database.repository.base import BaseRepository


class BaseService[
    CreateSchemaType: BaseModel,
    UpdateSchemaType: BaseModel,
    ReadSchemaType: BaseModel,
]:
    def __init__(
        self,
        repository: BaseRepository[Base, CreateSchemaType, ReadSchemaType],
        read_entity: Type[ReadSchemaType],
    ) -> None:
        self._repository = repository
        self._read_entity = read_entity

    async def get_multi(self, query: Type[BaseQuery]) -> list[ReadSchemaType]:
        result = await self._repository.get_multi(query)
        return self._read_entity.from_list(result)

    async def get_by_id(self, entity_id: UUID | str) -> ReadSchemaType:
        result = await self._repository.get_by_id(entity_id)
        if not result:
            raise NotFoundError()
        return self._read_entity.model_validate(result)

    async def create(self, entity: CreateSchemaType) -> ReadSchemaType:
        result = await self._repository.create(entity)
        return self._read_entity.model_validate(result)

    async def update_by_id(
        self,
        entity_id: UUID,
        entity: UpdateSchemaType,
    ) -> ReadSchemaType:
        result = await self._repository.update_by_id(entity_id, entity)
        if not result:
            raise NotFoundError()
        return self._read_entity.model_validate(result)

    async def delete_by_id(self, entity_id: UUID) -> None:
        await self._repository.delete_by_id(entity_id)
