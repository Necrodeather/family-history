from uuid import UUID

from app.domain.exceptions import NotFoundError
from app.domain.service.crud import CRUDService
from app.domain.types import (
    CreateSchemaType,
    ReadSchemaType,
    UpdateSchemaType,
)


class AppCRUDService(
    CRUDService[
        CreateSchemaType,
        UpdateSchemaType,
        ReadSchemaType,
    ]
):
    async def get_all(self) -> list[ReadSchemaType]:
        async with self._uow as uow:
            result = await uow.repository.get_all()
        return self._read_entity.from_list(result)

    async def get_by_id(self, entity_id: UUID | str) -> ReadSchemaType:
        async with self._uow as uow:
            result = await uow.repository.get_by_id(entity_id)
        if not result:
            raise NotFoundError()
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
        if not result:
            raise NotFoundError()
        return self._read_entity.model_validate(result)

    async def delete_by_id(self, entity_id: UUID) -> None:
        async with self._uow as uow:
            await uow.repository.delete_by_id(entity_id)
