from domain.entities.budget import BudgetCreate, BudgetUpdate
from infrastructure.database.models.budget import Expenses, Income
from infrastructure.database.repository.base import (
    BaseRepository,
)


class ExpensesRepository(BaseRepository[Expenses, BudgetCreate, BudgetUpdate]):
    """Repository for expenses."""
    pass


class IncomeRepository(BaseRepository[Income, BudgetCreate, BudgetUpdate]):
    """Repository for income."""
    pass
