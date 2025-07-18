from app.domain.entities.category import CategoryCreateUpdateForm, CategoryRead
from app.infrastructure.database.repository.crud.category import (
    expenses_category_crud,
    income_category_crud,
)
from app.infrastructure.database.uow import SqlAlchemyUnitOfWork
from app.service.base import AppCRUDService


class CategoryService(
    AppCRUDService[
        CategoryCreateUpdateForm,
        CategoryCreateUpdateForm,
        CategoryRead,
    ]
):
    pass


expenses_category_service = CategoryService(
    SqlAlchemyUnitOfWork(expenses_category_crud),
    CategoryRead,
)
income_category_service = CategoryService(
    SqlAlchemyUnitOfWork(income_category_crud),
    CategoryRead,
)
