from typing import Sequence

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.domain.entities.category import (
    CategoryCreateForm,
    CategoryRead,
    CategoryUpdateForm,
)
from app.infrastructure.database.models.budget import ExpensesCategory
from app.infrastructure.database.models.user import User
from app.public.api.schemas import CategoryQueryApi
from tests.public.api.v1.base import (
    create_entity,
    delete_entity,
    get_entities,
    get_entity_by_id,
    update_entity,
)

pytestmark = pytest.mark.asyncio


@pytest.fixture
def endpoint_url() -> str:
    return '/api/v1/budget/expenses_category/'


async def test_get_expenses_categories(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses_categories: Sequence[ExpensesCategory],
    category_query: CategoryQueryApi,
    mock_execute: MockerFixture,
) -> None:
    await get_entities(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entities=expenses_categories,
        query=category_query,
        sql_execute=mock_execute,
        read_schema=CategoryRead,
    )


async def test_get_expenses_category_by_id(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses_category: ExpensesCategory,
    mock_execute: MockerFixture,
) -> None:
    await get_entity_by_id(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenses_category,
        sql_execute=mock_execute,
        read_schema=CategoryRead,
    )


async def test_create_expenses_category(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses_category: ExpensesCategory,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    expenses_category_register = CategoryCreateForm(
        name=expenses_category.name,
    ).model_dump()

    await create_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenses_category,
        entity_register=expenses_category_register,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=CategoryRead,
    )


async def test_update_expenses_category(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses_category: ExpensesCategory,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    await update_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenses_category,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=CategoryRead,
        update_schema=CategoryUpdateForm,
    )


async def test_delete_expenses_category(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses_category: ExpensesCategory,
    mock_execute: MockerFixture,
) -> None:
    await delete_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenses_category,
        sql_execute=mock_execute,
    )
