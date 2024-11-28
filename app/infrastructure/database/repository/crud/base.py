from typing import Any, Self, Sequence, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repository.crud import (
    CRUDRepository,
)
from app.domain.types import (
    CreateSchemaType,
    ModelType,
    UpdateSchemaType,
)
from app.infrastructure.database.base import Base

AlchemyModelType = TypeVar('AlchemyModelType', bound=Base)


class SQLAlchemyCRUDRepository(
    CRUDRepository[
        ModelType,
        CreateSchemaType,
        UpdateSchemaType,
    ],
):
    def __init__(self, model: type[AlchemyModelType]) -> None:
        self._model = model

    def __call__(self, session: AsyncSession) -> Self:
        self.session = session
        return self

    async def get_all(
        self,
    ) -> Sequence[ModelType]:
        stmt = select(self._model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(
        self,
        obj_id: Any,
    ) -> ModelType | None:
        stmt = select(self._model).where(self._model.id == obj_id)
        result = await self.session.execute(stmt)
        return result.scalars().one_or_none()

    async def create(self, object: CreateSchemaType) -> ModelType:
        stmt = (
            insert(self._model)
            .values(object.model_dump())
            .returning(self._model)
        )
        result = await self.session.execute(stmt)
        return result.scalar()

    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: UpdateSchemaType,
    ) -> ModelType:
        stmt = (
            update(self._model)
            .where(self._model.id == obj_id)
            .values(obj_data)
            .returning(self._model)
        )
        result = await self.session.execute(stmt)
        return result.scalar()

    async def delete_by_id(self, entity_id: Any) -> None:
        stmt = delete(self._model).where(self._model.id == entity_id)
        await self.session.execute(stmt)
