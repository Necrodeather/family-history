from app.domain.entities.budget import BudgetCreateUpdateForm, BudgetRead
from app.infrastructure.database.models.budget import Expenses, Income
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class CRUDExpenses(
    SQLAlchemyCRUDRepository[Expenses, BudgetCreateUpdateForm, BudgetRead]
):
    pass


class CRUDIncome(
    SQLAlchemyCRUDRepository[Income, BudgetCreateUpdateForm, BudgetRead]
):
    pass


expenses_crud = CRUDExpenses(Expenses)
income_crud = CRUDIncome(Expenses)
