import pytest
from pytest_mock import MockerFixture

from app.domain.entities.category import CategoryCreateForm
from app.domain.exceptions import EntityAlreadyError
from app.infrastructure.database.models.budget import ExpensesCategory
from app.service.category import (
    expenses_category_service,
    income_category_service,
)

pytestmark = pytest.mark.asyncio


async def test_expenses_category_service_error(
    expenses_category: ExpensesCategory,
    mock_execute: MockerFixture,
) -> None:
    mock_execute(raise_error=True)
    expenses_category_create = CategoryCreateForm(
        name=expenses_category.name,
        user_id=expenses_category.user_id,
    )
    with pytest.raises(EntityAlreadyError):
        await expenses_category_service.create(expenses_category_create)


async def test_income_category_service_error(
    income_category: ExpensesCategory,
    mock_execute: MockerFixture,
) -> None:
    mock_execute(raise_error=True)
    income_category_create = CategoryCreateForm(
        name=income_category.name,
        user_id=income_category.user_id,
    )
    with pytest.raises(EntityAlreadyError):
        await income_category_service.create(income_category_create)
