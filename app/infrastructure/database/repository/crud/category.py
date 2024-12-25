from app.domain.entities.category import CategoryCreateUpdateForm
from app.infrastructure.database.models.budget import (
    ExpensesCategory,
    IncomesCategory,
)
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class CRUDExpensesCategory(
    SQLAlchemyCRUDRepository[
        ExpensesCategory,
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
    ]
):
    pass


class CRUDIncomesCategory(
    SQLAlchemyCRUDRepository[
        IncomesCategory,
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
    ]
):
    pass


expenses_category_crud = CRUDExpensesCategory(ExpensesCategory)
income_category_crud = CRUDIncomesCategory(IncomesCategory)
