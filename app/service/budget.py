from app.domain.entities.budget import BudgetCreateUpdateForm, BudgetRead
from app.infrastructure.database.repository.crud.budget import (
    expenses_crud,
    income_crud,
)
from app.infrastructure.database.uow import SqlAlchemyUnitOfWork
from app.service.base import BaseService


class BudgetService(
    BaseService[
        BudgetCreateUpdateForm,
        BudgetCreateUpdateForm,
        BudgetRead,
    ]
):
    pass


income_service = BudgetService(SqlAlchemyUnitOfWork(expenses_crud), BudgetRead)
income_service = BudgetService(SqlAlchemyUnitOfWork(income_crud), BudgetRead)
