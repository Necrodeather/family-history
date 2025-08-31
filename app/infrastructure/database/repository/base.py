from typing import Any, Sequence, Type

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
    text,
    update,
)
from sqlalchemy.orm import joinedload, selectinload

from domain.entities.queries import BaseQuery
from infrastructure.database.base import Base
from infrastructure.database.engine import SqlAlchemyEngine
from infrastructure.database.filter.base import BaseFilter


class BaseRepository[
    ModelType: Base,
    CreateSchemaType: BaseModel,
    UpdateSchemaType: BaseModel,
]:
    """Base class for all repositories."""

    def __init__(
        self,
        engine: SqlAlchemyEngine,
        model: Type[ModelType],
        filter: BaseFilter,
    ) -> None:
        """Initializes the repository.

        :param engine: The database engine.
        :type engine: SqlAlchemyEngine
        :param model: The database model.
        :type model: Type[ModelType]
        :param filter: The filter for the model.
        :type filter: BaseFilter
        """
        self._model = model
        self._engine = engine
        self._filter = filter

    async def get_multi(
        self,
        query: Type[BaseQuery],
    ) -> Sequence[ModelType]:
        """Gets multiple records from the database.

        :param query: The query to filter the records.
        :type query: Type[BaseQuery]
        :returns: A list of records.
        :rtype: Sequence[ModelType]
        """
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
        """Gets a record by its ID.

        :param obj_id: The ID of the record.
        :type obj_id: Any
        :returns: The record, or None if it does not exist.
        :rtype: ModelType | None
        """
        stmt = select(self._model).where(self._model.id == obj_id)
        stmt = self._get_joinedload(stmt)

        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalars().one_or_none()

    async def create(self, object: CreateSchemaType) -> ModelType:
        """Creates a new record.

        :param object: The data to create the record with.
        :type object: CreateSchemaType
        :returns: The created record.
        :rtype: ModelType
        """
        stmt = (
            insert(self._model)
            .values(object.model_dump())
            .returning(self._model)
        )
        stmt = self._get_selectinload(stmt)

        async with self._engine.session() as session:
            async with session.begin():
                result = await session.execute(stmt)
                await session.commit()
        return result.scalar()

    async def update_by_id(
        self,
        obj_id: Any,
        obj_data: UpdateSchemaType,
    ) -> ModelType:
        """Updates a record by its ID.

        :param obj_id: The ID of the record to update.
        :type obj_id: Any
        :param obj_data: The data to update the record with.
        :type obj_data: UpdateSchemaType
        :returns: The updated record.
        :rtype: ModelType
        """
        stmt = (
            update(self._model)
            .where(self._model.id == obj_id)
            .values(obj_data.model_dump(exclude_none=True))
            .returning(self._model)
        )
        stmt = self._get_selectinload(stmt)
        async with self._engine.session() as session:
            async with session.begin():
                result = await session.execute(stmt)
                await session.commit()
        return result.scalar()

    async def delete_by_id(self, entity_id: Any) -> None:
        """Deletes a record by its ID.

        :param entity_id: The ID of the record to delete.
        :type entity_id: Any
        """
        stmt = delete(self._model).where(self._model.id == entity_id)
        async with self._engine.session() as session:
            await session.execute(stmt)

    def _order_by(self, order: str | None) -> UnaryExpression | None:
        """Creates an order by expression.

        :param order: The order to sort by.
        :type order: str | None
        :returns: An order by expression.
        :rtype: UnaryExpression | None
        """
        if not order:
            return None

        if order.startswith('-'):
            order = order[1:]
            return desc(text(order))

        return asc(text(order))

    def _get_joinedload(self, stmt: Select) -> Select:
        """Adds a joined load to a query.

        :param stmt: The query to add the joined load to.
        :type stmt: Select
        :returns: The query with the joined load.
        :rtype: Select
        """
        for rel in inspect(self._model).relationships:
            stmt = stmt.options(joinedload(getattr(self._model, rel.key)))
        return stmt

    def _get_selectinload(self, stmt: Select) -> Select:
        """Adds a select in load to a query.

        :param stmt: The query to add the select in load to.
        :type stmt: Select
        :returns: The query with the select in load.
        :rtype: Select
        """
        for rel in inspect(self._model).relationships:
            stmt = stmt.options(selectinload(getattr(self._model, rel.key)))
        return stmt
