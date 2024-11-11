from app.domain.entities.category import CategoryCreateUpdateForm, CategoryRead
from app.infrastructure.database.models.budget import (
    ExpensesCategory,
    IncomesCategory,
)
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class CRUDExpensesCategory(
    SQLAlchemyCRUDRepository[  # type: ignore[type-arg]
        ExpensesCategory,
        CategoryCreateUpdateForm,
        CategoryRead,
    ]
):
    pass


class CRUDIncomesCategory(
    SQLAlchemyCRUDRepository[  # type: ignore[type-arg]
        IncomesCategory,
        CategoryCreateUpdateForm,
        CategoryRead,
    ]
):
    pass


expenses_category_crud = CRUDExpensesCategory(ExpensesCategory)
income_category_crud = CRUDIncomesCategory(IncomesCategory)
