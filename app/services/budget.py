from domain.entities.budget import (
    BudgetCreate,
    BudgetRead,
    BudgetUpdate,
)

from .base import BaseService


class BudgetService(
    BaseService[
        BudgetCreate,
        BudgetUpdate,
        BudgetRead,
    ]
):
    """Service for budgets."""
    pass
