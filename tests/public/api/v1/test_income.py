from typing import Sequence

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.domain.entities.budget import (
    BudgetCreateForm,
    BudgetRead,
    BudgetUpdateForm,
)
from app.infrastructure.database.models.budget import Income
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
    return '/api/v1/budget/income/'


async def test_get_incomes(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    incomes: Sequence[Income],
    budget_query: BudgetQueryApi,
    mock_execute: MockerFixture,
) -> None:
    await get_entities(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entities=incomes,
        query=budget_query,
        sql_execute=mock_execute,
        read_schema=BudgetRead,
    )


async def test_get_income_by_id(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    income: Income,
    mock_execute: MockerFixture,
) -> None:
    await get_entity_by_id(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=income,
        sql_execute=mock_execute,
        read_schema=BudgetRead,
    )


async def test_create_income(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    income: Income,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    income_register = BudgetCreateForm(
        name=income.name,
        category_id=income.category_id,
        date=income.date,
        amount=income.amount,
    ).model_dump(mode='json')

    await create_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=income,
        entity_register=income_register,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=BudgetRead,
    )


async def test_update_income(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    income: Income,
    mock_execute: MockerFixture,
    user: User,
    mock_jwt_decode: MockerFixture,
) -> None:
    await update_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=income,
        jwt_decode=mock_jwt_decode,
        sql_execute=mock_execute,
        user=user,
        read_schema=BudgetRead,
        update_schema=BudgetUpdateForm,
    )


async def test_delete_income(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    income: Income,
    mock_execute: MockerFixture,
) -> None:
    await delete_entity(
        http_client=authenticated_http_client,
        url=endpoint_url,
        entity=income,
        sql_execute=mock_execute,
    )
