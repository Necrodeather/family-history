from fastapi import Query
from pydantic import BaseModel

from app.domain.entities.budget import BudgetQuery
from app.domain.entities.category import CategoryQuery
from app.domain.entities.user import UserQuery


class ErrorMessage(BaseModel):
    message: str


class CategoryQueryApi(CategoryQuery):
    name__like: str | None = Query(default=None)


class BudgetQueryApi(BudgetQuery):
    name__like: str | None = Query(default=None)
    category_id: int | None = Query(default=None)
    user_id: int | None = Query(default=None)


class UserQueryApi(UserQuery):
    name__like: str | None = Query(default=None)
