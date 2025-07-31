from sqlalchemy.exc import IntegrityError

from domain.entities.category import CategoryCreate
from domain.exceptions import EntityAlreadyError
from infrastructure.database.models.category import (
    ExpensesCategory,
    IncomesCategory,
)
from infrastructure.database.repository.base import (
    BaseRepository,
)


class ExpensesCategoryRepository(
    BaseRepository[
        ExpensesCategory,
        CategoryCreate,
        CategoryCreate,
    ]
):
    async def create(
        self,
        object: CategoryCreate,
    ) -> ExpensesCategory:
        try:
            return await super().create(object)
        except IntegrityError:
            raise EntityAlreadyError()


class IncomesCategoryRepository(
    BaseRepository[
        IncomesCategory,
        CategoryCreate,
        CategoryCreate,
    ]
):
    async def create(
        self,
        object: CategoryCreate,
    ) -> IncomesCategory:
        try:
            return await super().create(object)
        except IntegrityError:
            raise EntityAlreadyError()
