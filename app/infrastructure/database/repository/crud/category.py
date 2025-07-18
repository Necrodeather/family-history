from sqlalchemy.exc import IntegrityError

from app.domain.entities.category import CategoryCreateUpdateForm
from app.domain.exceptions import EntityAlreadyError
from app.infrastructure.database.models.budget import (
    ExpensesCategory,
    IncomesCategory,
)
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)
from app.infrastructure.database.repository.filter.budget import (
    expenses_category_filter,
    income_category_filter,
)


class CRUDExpensesCategory(
    SQLAlchemyCRUDRepository[
        ExpensesCategory,
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
    ]
):
    async def create(
        self,
        object: CategoryCreateUpdateForm,
    ) -> ExpensesCategory:
        try:
            return await super().create(object)
        except IntegrityError:
            raise EntityAlreadyError()


class CRUDIncomesCategory(
    SQLAlchemyCRUDRepository[
        IncomesCategory,
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
    ]
):
    async def create(
        self,
        object: CategoryCreateUpdateForm,
    ) -> IncomesCategory:
        try:
            return await super().create(object)
        except IntegrityError:
            raise EntityAlreadyError()


expenses_category_crud = CRUDExpensesCategory(
    ExpensesCategory,
    expenses_category_filter,
)
income_category_crud = CRUDIncomesCategory(
    IncomesCategory,
    income_category_filter,
)
