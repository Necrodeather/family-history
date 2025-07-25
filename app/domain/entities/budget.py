# Error in type Optional[date]! FIX: alias import
from datetime import date as date_type
from datetime import datetime
from decimal import Decimal

from pydantic import UUID4, BaseModel

from app.domain.entities.base import BaseEntity
from app.domain.entities.user import UserRelation


class BudgetCreate(BaseModel):
    name: str
    category_id: UUID4
    amount: Decimal
    date: date_type
    user_id: UUID4 | None = None


class BudgetUpdate(BaseModel):
    name: str | None = None
    category_id: UUID4 | None = None
    amount: Decimal | None = None
    date: date_type | None = None
    updated_user_id: UUID4 | None = None


class BudgetRead(BudgetCreate, BaseEntity):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    user_id: UUID4
    user: UserRelation
    update_user: UserRelation | None
