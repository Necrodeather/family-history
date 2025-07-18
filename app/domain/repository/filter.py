from abc import abstractmethod
from typing import Any


class QueryFilter:
    @property
    def select(self) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def where(self, query: Any) -> Any:
        raise NotImplementedError()

    @property
    def order_by(self) -> Any:
        raise NotImplementedError()

    @property
    def limit(self) -> Any:
        raise NotImplementedError()

    @property
    def offset(self) -> Any:
        raise NotImplementedError()
