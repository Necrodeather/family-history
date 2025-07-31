from datetime import datetime

from pydantic import UUID4, BaseModel

from domain.entities.base import BaseEntity
from domain.entities.user import UserRelation


class CategoryCreate(BaseModel):
    name: str
    user_id: UUID4 | None = None


class CategoryUpdate(BaseModel):
    name: str
    updated_user_id: UUID4 | None = None


class CategoryRead(CategoryCreate, CategoryUpdate, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    user: UserRelation
    updated_user: UserRelation | None
