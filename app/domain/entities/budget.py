# Error in type Optional[date]! FIX: alias import
from datetime import date as date_type
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4, BaseModel, Field

from domain.entities.base import BaseEntity
from domain.entities.user import UserRelation


class BudgetCreate(BaseModel):
    """Represents a budget to be created."""
    name: str = Field(description='Name of the budget')
    category_id: UUID4 = Field(description='Category ID of the budget')
    amount: Decimal = Field(description='Amount of the budget')
    date: date_type = Field(description='Date of the budget')
    user_id: UUID4 | None = Field(
        description='User ID of the budget',
        default=None,
    )


class BudgetUpdate(BaseModel):
    """Represents a budget to be updated."""
    name: str | None = Field(
        default=None,
        description='New name of the budget',
    )
    category_id: UUID4 | None = Field(
        default=None,
        description='New category ID of the budget',
    )
    amount: Decimal | None = Field(
        default=None,
        description='New amount of the budget',
    )
    date: date_type | None = Field(
        default=None,
        description='New date of the budget',
    )
    updated_user_id: UUID4 | None = Field(
        default=None,
        description='User ID who updated the budget',
    )


class BudgetRead(BudgetCreate, BaseEntity):
    """Represents a budget that has been read from the database."""
    id: UUID4 = Field(description='Unique identifier for the budget')
    created_at: datetime = Field(
        description='Timestamp when the budget was created'
    )
    updated_at: datetime = Field(
        description='Timestamp when the budget was last updated'
    )
    user_id: UUID4 = Field(description='User ID associated with the budget')
    user: UserRelation = Field(
        description='User relation object for the budget'
    )
    update_user: UserRelation | None = Field(
        default=None,
        description='User relation object who updated the budget',
    )
