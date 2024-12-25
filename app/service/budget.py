from app.domain.entities.budget import (
    BudgetCreateForm,
    BudgetRead,
    BudgetUpdateForm,
)
from app.infrastructure.database.repository.crud.budget import (
    expenses_crud,
    income_crud,
)
from app.infrastructure.database.uow import SqlAlchemyUnitOfWork
from app.service.base import AppCRUDService


class BudgetService(
    AppCRUDService[
        BudgetCreateForm,
        BudgetUpdateForm,
        BudgetRead,
    ]
):
    pass


expenses_service = BudgetService(
    SqlAlchemyUnitOfWork(expenses_crud),
    BudgetRead,
)
income_service = BudgetService(
    SqlAlchemyUnitOfWork(income_crud),
    BudgetRead,
)
