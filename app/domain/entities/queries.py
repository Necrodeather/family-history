from pydantic import BaseModel, Field, ValidationInfo, field_validator

MAX_PER_PAGE = 50
MIN_PER_PAGE = 25


class BaseQuery(BaseModel):
    name__like: str | None = Field(
        serialization_alias='name',
        default=None,
    )
    order: str | None = None
    per_page: int = MIN_PER_PAGE
    page: int | None = None

    @field_validator('per_page')
    @classmethod
    def limit_per_page(cls, value: int) -> int:
        return MAX_PER_PAGE if value >= MAX_PER_PAGE else MIN_PER_PAGE

    @field_validator('page')
    @classmethod
    def offset(cls, value: int | None, values: ValidationInfo) -> int | None:
        return (value - 1) * int(values.data['per_page']) if value else None


class CategoryQuery(BaseQuery):
    pass


class BudgetQuery(BaseQuery):
    category_id: str | None = None
    user_id: str | None = None


class UserQuery(BaseQuery):
    pass
