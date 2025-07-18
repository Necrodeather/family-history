from typing import Type

from sqlalchemy import (
    BinaryExpression,
    Select,
    UnaryExpression,
    asc,
    desc,
    select,
)

from app.domain.repository.filter import QueryFilter
from app.domain.types import ModelType, QuerySchemaType


class SqlAlchemyFilter(QueryFilter):
    def __init__(
        self,
        model: Type[ModelType],
    ):
        super().__init__()

        self._model = model

        self.page: int | None = None
        self.per_page = 25
        self.order: str | None = None

    @property
    def select(self) -> Select:
        return select(self._model)

    def where(self, query: QuerySchemaType) -> BinaryExpression | None:
        return None

    @property
    def order_by(self) -> UnaryExpression | None:
        if self.order is None:
            return None

        order_function = asc
        order = self.order
        if order.startswith('-'):
            order = order[1:]
            order_function = desc

        return order_function(order)

    @property
    def limit(self) -> int:
        return self.per_page

    @property
    def offset(self) -> int | None:
        if self.page:
            return (self.page - 1) * self.per_page

        return None
