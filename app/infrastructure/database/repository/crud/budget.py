from app.domain.entities.budget import BudgetCreateForm, BudgetUpdateForm
from app.infrastructure.database.models.budget import Expenses, Income
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)
from app.infrastructure.database.repository.filter.budget import (
    expenses_filter,
    income_filter,
)


class CRUDExpenses(
    SQLAlchemyCRUDRepository[Expenses, BudgetCreateForm, BudgetUpdateForm]
):
    pass


class CRUDIncome(
    SQLAlchemyCRUDRepository[Income, BudgetCreateForm, BudgetUpdateForm]
):
    pass


expenses_crud = CRUDExpenses(Expenses, expenses_filter)
income_crud = CRUDIncome(Expenses, income_filter)
