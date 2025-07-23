import pytest

from app.domain.entities.budget import BudgetQuery
from app.domain.entities.category import CategoryQuery
from app.infrastructure.database.repository.filter.budget import (
    income_category_filter,
    income_filter,
)
from tests.infrastructure.database.repository.filter.base import (
    filter_empty_query,
    filter_where,
)


@pytest.mark.parametrize(
    ('query', 'pydantic_key', 'filter_key'),
    [
        (BudgetQuery(name__like='test'), 'name__like', 'name_1'),
        (BudgetQuery(category_id='test'), 'category_id', 'category_id_1'),
        (BudgetQuery(user_id='test'), 'user_id', 'user_id_1'),
    ],
)
def test_budget_filter_where(
    query: BudgetQuery,
    pydantic_key: str,
    filter_key: str,
) -> None:
    filter_where(income_filter, query, pydantic_key, filter_key)


def test_budget_filter_empty_query() -> None:
    query = BudgetQuery()
    filter_empty_query(income_filter, query)


def test_category_filter_where() -> None:
    filter_where(
        income_category_filter,
        CategoryQuery(name__like='test'),
        'name__like',
        'name_1',
    )


def test_category_filter_empty_query() -> None:
    query = CategoryQuery()
    filter_empty_query(income_category_filter, query)
