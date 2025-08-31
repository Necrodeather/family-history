from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from domain.entities.base import BaseEntity
from domain.entities.user import UserRelation


class CategoryCreate(BaseModel):
    """Represents a category to be created."""
    name: str = Field(description='The name of the category')
    user_id: UUID4 | None = Field(
        default=None,
        description='The ID of the user who created the category',
    )


class CategoryUpdate(BaseModel):
    """Represents a category to be updated."""
    name: str = Field(description='The updated name of the category')
    updated_user_id: UUID4 | None = Field(
        None,
        description='The ID of the user who last updated the category',
    )


class CategoryRead(CategoryCreate, CategoryUpdate, BaseEntity):
    """Represents a category that has been read from the database."""
    id: UUID4 = Field(description='The unique identifier for the category')
    created_at: datetime = Field(
        description='The date and time when the category was created'
    )
    updated_at: datetime = Field(
        description='The date and time when the category was last updated'
    )
    user: UserRelation = Field(description='The user who created the category')
    updated_user: UserRelation | None = Field(
        default=None,
        description='The user who last updated the category, if applicable',
    )
