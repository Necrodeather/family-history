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
    """Repository for expenses categories."""

    async def create(
        self,
        object: CategoryCreate,
    ) -> ExpensesCategory:
        """Creates a new expenses category.

        :param object: The data to create the category with.
        :type object: CategoryCreate
        :raises EntityAlreadyError: If a category with the same name
        already exists.
        :returns: The created category.
        :rtype: ExpensesCategory
        """
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
    """Repository for incomes categories."""

    async def create(
        self,
        object: CategoryCreate,
    ) -> IncomesCategory:
        """Creates a new incomes category.

        :param object: The data to create the category with.
        :type object: CategoryCreate
        :raises EntityAlreadyError: If a category with the same name
        already exists.
        :returns: The created category.
        :rtype: IncomesCategory
        """
        try:
            return await super().create(object)
        except IntegrityError:
            raise EntityAlreadyError()
