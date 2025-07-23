from typing import Any, Sequence
from unittest.mock import AsyncMock, Mock

import pytest
from pytest_mock import MockerFixture
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models.budget import (
    Expenses,
    ExpensesCategory,
    Income,
    IncomesCategory,
)
from app.infrastructure.database.models.user import User
from tests.factories.models.budget import (
    ExpensesCategoryFactory,
    ExpensesFactory,
    IncomeFactory,
    IncomesCategoryFactory,
)
from tests.factories.models.user import UserFactory


@pytest.fixture
def mock_execute(mocker: MockerFixture) -> MockerFixture:
    def _mock_execute(
        scalar: Any = None,
        scalars_all: Any = None,
        scalars_one_or_none: Any = None,
        raise_error: bool = False,
    ) -> AsyncMock | None:
        if raise_error:
            mocker.patch(
                'sqlalchemy.ext.asyncio.AsyncSession.execute',
                side_effect=IntegrityError('duplicate key', {}, None),
            )
            return None

        mocked_result = AsyncMock()

        if scalar:
            mocked_result.scalar = Mock(return_value=scalar)

        if scalars_all:
            scalars = Mock()
            scalars.all = Mock(return_value=scalars_all)
            mocked_result.scalars = Mock(return_value=scalars)

        if scalars_one_or_none:
            scalars = Mock()
            scalars.one_or_none = Mock(return_value=scalars_one_or_none)
            mocked_result.scalars = Mock(return_value=scalars)

        mocker.patch(
            'sqlalchemy.ext.asyncio.AsyncSession.execute',
            return_value=mocked_result,
        )

        return mocked_result

    return _mock_execute


@pytest.fixture(scope='session')
def user() -> User:
    return UserFactory.build()


@pytest.fixture(scope='session')
def users() -> Sequence[User]:
    return UserFactory.build_batch(25)


@pytest.fixture(scope='session')
def expenses_category() -> ExpensesCategory:
    return ExpensesCategoryFactory.build()


@pytest.fixture(scope='session')
def expenses_categories() -> Sequence[ExpensesCategory]:
    return ExpensesCategoryFactory.build_batch(25)


@pytest.fixture(scope='session')
def income_category() -> IncomesCategory:
    return IncomesCategoryFactory.build()


@pytest.fixture(scope='session')
def income_categories() -> Sequence[IncomesCategory]:
    return IncomesCategoryFactory.build_batch(25)


@pytest.fixture(scope='session')
def expenditure() -> Expenses:
    return ExpensesFactory.build()


@pytest.fixture(scope='session')
def expenses() -> Sequence[Expenses]:
    return ExpensesFactory.build_batch(25)


@pytest.fixture(scope='session')
def income() -> Income:
    return IncomeFactory.build()


@pytest.fixture(scope='session')
def incomes() -> Sequence[Income]:
    return IncomeFactory.build_batch(25)

