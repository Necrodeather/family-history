from app.domain.entities.budget import BudgetCreate, BudgetUpdate
from app.infrastructure.database.models.budget import Expenses, Income
from app.infrastructure.database.repository.base import (
    BaseRepository,
)


class ExpensesRepository(BaseRepository[Expenses, BudgetCreate, BudgetUpdate]):
    pass


class IncomeRepository(BaseRepository[Income, BudgetCreate, BudgetUpdate]):
    pass
