from abc import ABC, abstractmethod
from typing import Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import BinaryExpression

from infrastructure.database.base import Base

ModelType = TypeVar('ModelType', bound=Base)
QueryType = TypeVar('QueryType', bound=BaseModel)


class BaseFilter(ABC):
    def __init__(
        self,
        model: Type[ModelType],
    ) -> None:
        self._model = model

    @abstractmethod
    def where(self, query: QueryType) -> BinaryExpression | None:
        return None
