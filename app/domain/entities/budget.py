from datetime import date, datetime
from decimal import Decimal

from pydantic import UUID4, BaseModel

from app.domain.entities.base import BaseEntity


class BudgetCreateUpdateForm(BaseModel):
    name: str
    category_id: UUID4
    amount: Decimal
    date: date


class BudgetRead(BudgetCreateUpdateForm, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime
