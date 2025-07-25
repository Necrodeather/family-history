from typing import Any, Sequence, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import (
    Select,
    UnaryExpression,
    asc,
    delete,
    desc,
    insert,
    inspect,
    select,
    update,
)
from sqlalchemy.orm import joinedload, selectinload

from app.domain.entities.queries import BaseQuery
from app.infrastructure.database.base import Base
from app.infrastructure.database.engine import SqlAlchemyEngine
from app.infrastructure.database.filter.base import BaseFilter

AlchemyModelType = TypeVar('AlchemyModelType', bound=Base)


class BaseRepository[
    ModelType: BaseModel,
    CreateSchemaType: BaseModel,
    UpdateSchemaType: BaseModel,
]:
    def __init__(
        self,
        engine: SqlAlchemyEngine,
        model: Type[AlchemyModelType],
        filter: BaseFilter,
    ) -> None:
        self._model = model
        self._engine = engine
        self._filter = filter

    async def get_multi(
        self,
        query: Type[BaseQuery],
    ) -> Sequence[ModelType]:
        stmt = select(self._model).limit(query.per_page)

        stmt = self._get_joinedload(stmt)

        where_expression = self._filter.where(query)
        if where_expression is not None:
            stmt = stmt.where(where_expression)

        order_by = self._order_by(query.order)
        if order_by is not None:
            stmt = stmt.order_by(order_by)

        if query.page:
            stmt = stmt.offset(query.page)

        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(
        self,
        obj_id: Any,
    ) -> ModelType | None:
        stmt = select(self._model).where(self._model.id == obj_id)
        stmt = self._get_joinedload(stmt)

        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalars().one_or_none()

    async def create(self, object: CreateSchemaType) -> ModelType:
        stmt = (
            insert(self._model)
            .values(object.model_dump())
            .returning(self._model)
        )
        stmt = self._get_selectinload(stmt)

        async with self._engine.session() as session:
            result = await session.execute(stmt)
            await session.commit()
        return result.scalar()

    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: UpdateSchemaType,
    ) -> ModelType:
        stmt = (
            update(self._model)
            .where(self._model.id == obj_id)
            .values(obj_data.model_dump(exclude_none=True))
            .returning(self._model)
        )
        stmt = self._get_selectinload(stmt)
        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalar()

    async def delete_by_id(self, entity_id: Any) -> None:
        stmt = delete(self._model).where(self._model.id == entity_id)
        async with self._engine.session() as session:
            await session.execute(stmt)

    def _order_by(self, order: str | None) -> UnaryExpression | None:
        if order is None:
            return None

        if order.startswith('-'):
            order = order[1:]
            return desc(order)

        return asc(order)

    def _get_joinedload(self, stmt: Select) -> Select:
        for rel in inspect(self._model).relationships:
            stmt = stmt.options(joinedload(getattr(self._model, rel.key)))
        return stmt

    def _get_selectinload(self, stmt: Select) -> Select:
        for rel in inspect(self._model).relationships:
            stmt = stmt.options(selectinload(getattr(self._model, rel.key)))
        return stmt
