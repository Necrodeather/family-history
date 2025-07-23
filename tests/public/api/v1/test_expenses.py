from typing import Sequence

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.domain.entities.budget import (
    BudgetCreateForm,
    BudgetRead,
    BudgetUpdateForm,
)
from app.infrastructure.database.models.budget import Expenses
from app.infrastructure.database.models.user import User
from app.public.api.schemas import BudgetQueryApi
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
    return '/api/v1/budget/expenses/'


async def test_get_expenses(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenses: Sequence[Expenses],
    budget_query: BudgetQueryApi,
    mock_execute: MockerFixture,
) -> None:
    await get_entities(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entities=expenses,
        query=budget_query,
        sql_execute=mock_execute,
        read_schema=BudgetRead,
    )


async def test_get_expenses_by_id(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenditure: Expenses,
    mock_execute: MockerFixture,
) -> None:
    await get_entity_by_id(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenditure,
        sql_execute=mock_execute,
        read_schema=BudgetRead,
    )


async def test_create_expenses(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenditure: Expenses,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    expenses_register = BudgetCreateForm(
        name=expenditure.name,
        category_id=expenditure.category_id,
        date=expenditure.date,
        amount=expenditure.amount,
    ).model_dump(mode='json')

    await create_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenditure,
        entity_register=expenses_register,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=BudgetRead,
    )


async def test_update_expenses(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenditure: Expenses,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    await update_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenditure,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=BudgetRead,
        update_schema=BudgetUpdateForm,
    )


async def test_delete_expenses(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    expenditure: Expenses,
    mock_execute: MockerFixture,
) -> None:
    await delete_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=expenditure,
        sql_execute=mock_execute,
    )
