from app.domain.entities.category import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
)
from app.service.base import BaseService


class CategoryService(
    BaseService[
        CategoryCreate,
        CategoryUpdate,
        CategoryRead,
    ]
):
    pass
