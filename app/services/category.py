from domain.entities.category import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
)

from .base import BaseService


class CategoryService(
    BaseService[
        CategoryCreate,
        CategoryUpdate,
        CategoryRead,
    ]
):
    """Service for categories."""
    pass
