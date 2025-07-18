# Error in type Optional[date]! FIX: alias import
from datetime import date as date_type
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4, BaseModel

from app.domain.entities.base import BaseEntity


class BudgetCreateForm(BaseModel):
    name: str
    category_id: UUID4
    amount: Decimal
    date: date_type


class BudgetUpdateForm(BaseModel):
    name: str | None = None
    category_id: UUID4 | None = None
    amount: Decimal | None = None
    date: date_type | None = None


class BudgetRead(BudgetCreateForm, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime


class BudgetQuery(BaseModel):
    name__like: str | None
    category_id: int | None
    user_id: int | None
