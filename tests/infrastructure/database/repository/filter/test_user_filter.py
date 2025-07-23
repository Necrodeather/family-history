from app.domain.entities.user import UserQuery
from app.infrastructure.database.repository.filter.user import user_filter
from tests.infrastructure.database.repository.filter.base import (
    filter_empty_query,
    filter_where,
)


def test_category_filter_where() -> None:
    filter_where(
        user_filter,
        UserQuery(name__like='test'),
        'name__like',
        'first_name_1',
    )


def test_category_filter_empty_query() -> None:
    query = UserQuery()
    filter_empty_query(user_filter, query)
