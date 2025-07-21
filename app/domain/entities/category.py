from datetime import datetime

from pydantic import UUID4, BaseModel

from app.domain.entities.base import BaseEntity


class CategoryCreateForm(BaseModel):
    name: str
    user_id: UUID4 | None = None


class CategoryUpdateForm(BaseModel):
    name: str
    updated_user_id: UUID4 | None = None


class CategoryRead(CategoryCreateForm, CategoryUpdateForm, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime


class CategoryQuery(BaseModel):
    name__like: str | None
    page: int | None
    order: str | None
