from app.domain.entities.budget import BudgetCreateForm, BudgetUpdateForm
from app.infrastructure.database.models.budget import Expenses, Income
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class CRUDExpenses(
    SQLAlchemyCRUDRepository[Expenses, BudgetCreateForm, BudgetUpdateForm]
):
    pass


class CRUDIncome(
    SQLAlchemyCRUDRepository[Income, BudgetCreateForm, BudgetUpdateForm]
):
    pass


expenses_crud = CRUDExpenses(Expenses)
income_crud = CRUDIncome(Expenses)
