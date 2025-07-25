from app.domain.entities.budget import (
    BudgetCreate,
    BudgetRead,
    BudgetUpdate,
)
from app.service.base import BaseService


class BudgetService(
    BaseService[
        BudgetCreate,
        BudgetUpdate,
        BudgetRead,
    ]
):
    pass
