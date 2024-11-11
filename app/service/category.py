from app.domain.entities.category import CategoryCreateUpdateForm, CategoryRead
from app.infrastructure.database.repository.crud.category import (
    expenses_category_crud,
    incomes_category_crud,
)
from app.infrastructure.database.uow import SqlAlchemyUnitOfWork
from app.service.base import BaseService


class CategoryService(
    BaseService[
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
        CategoryRead,
    ]
):
    pass


expenses_category_service = CategoryService(
    SqlAlchemyUnitOfWork(expenses_category_crud), CategoryRead
)
incomes_category_service = CategoryService(
    SqlAlchemyUnitOfWork(incomes_category_crud), CategoryRead
)
