from typing import Type

import pytest

from app.domain.repositories.filter import QueryFilter
from app.domain.types import QuerySchemaType

pytestmark = pytest.mark.asyncio


def filter_where(
    filter: Type[QueryFilter],
    query: QuerySchemaType,
    pydantic_key: str,
    filter_key: str,
) -> None:
    query_assert = query.model_dump(
        exclude_none=True,
        exclude=['page', 'order'],
    )[pydantic_key]
    filter_query = filter.where(query).compile().params
    column = filter_query[filter_key].replace('%', '')
    assert column == query_assert


def filter_empty_query(
    filter: Type[QueryFilter],
    query: QuerySchemaType,
) -> None:
    assert filter.where(query) is None
