from typing import Type
from uuid import UUID

from pydantic import BaseModel

from domain.entities.queries import BaseQuery
from domain.exceptions import NotFoundError
from infrastructure.database.base import Base
from infrastructure.database.repository.base import BaseRepository


class BaseService[
    CreateSchemaType: BaseModel,
    UpdateSchemaType: BaseModel,
    ReadSchemaType: BaseModel,
]:
    """Base class for all services."""

    def __init__(
        self,
        repository: BaseRepository[Base, CreateSchemaType, ReadSchemaType],
        read_entity: Type[ReadSchemaType],
    ) -> None:
        """Initializes the service.

        :param repository: The repository for the service.
        :type repository: BaseRepository
        :param read_entity: The read entity for the service.
        :type read_entity: Type[ReadSchemaType]
        """
        self._repository = repository
        self._read_entity = read_entity

    async def get_multi(self, query: Type[BaseQuery]) -> list[ReadSchemaType]:
        """Gets multiple records.

        :param query: The query to filter the records.
        :type query: Type[BaseQuery]
        :returns: A list of records.
        :rtype: list[ReadSchemaType]
        """
        result = await self._repository.get_multi(query)
        return self._read_entity.from_list(result)

    async def get_by_id(self, entity_id: UUID | str) -> ReadSchemaType:
        """Gets a record by its ID.

        :param entity_id: The ID of the record.
        :type entity_id: UUID | str
        :raises NotFoundError: If the record does not exist.
        :returns: The record.
        :rtype: ReadSchemaType
        """
        result = await self._repository.get_by_id(entity_id)
        if not result:
            raise NotFoundError()
        return self._read_entity.model_validate(result)

    async def create(self, entity: CreateSchemaType) -> ReadSchemaType:
        """Creates a new record.

        :param entity: The data to create the record with.
        :type entity: CreateSchemaType
        :returns: The created record.
        :rtype: ReadSchemaType
        """
        result = await self._repository.create(entity)
        return self._read_entity.model_validate(result)

    async def update_by_id(
        self,
        entity_id: UUID,
        entity: UpdateSchemaType,
    ) -> ReadSchemaType:
        """Updates a record by its ID.

        :param entity_id: The ID of the record to update.
        :type entity_id: UUID
        :param entity: The data to update the record with.
        :type entity: UpdateSchemaType
        :raises NotFoundError: If the record does not exist.
        :returns: The updated record.
        :rtype: ReadSchemaType
        """
        result = await self._repository.update_by_id(entity_id, entity)
        if not result:
            raise NotFoundError()
        return self._read_entity.model_validate(result)

    async def delete_by_id(self, entity_id: UUID) -> None:
        """Deletes a record by its ID.

        :param entity_id: The ID of the record to delete.
        :type entity_id: UUID
        """
        await self._repository.delete_by_id(entity_id)
