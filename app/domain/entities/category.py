from datetime import datetime

from pydantic import UUID4, BaseModel

from app.domain.entities.base import BaseEntity


class CategoryCreateUpdateForm(BaseModel):
    name: str


class CategoryRead(CategoryCreateUpdateForm, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime


class CategoryQuery(BaseModel):
    name__like: str | None = None
