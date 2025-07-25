from sqlalchemy.exc import IntegrityError

from app.domain.entities.category import CategoryCreate
from app.domain.exceptions import EntityAlreadyError
from app.infrastructure.database.models.category import (
    ExpensesCategory,
    IncomesCategory,
)
from app.infrastructure.database.repository.base import (
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
