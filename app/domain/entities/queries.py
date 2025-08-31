from pydantic import BaseModel, Field, ValidationInfo, field_validator

MAX_PER_PAGE = 50
MIN_PER_PAGE = 25


class BaseQuery(BaseModel):
    """Base class for all query models."""

    name__like: str | None = Field(
        serialization_alias='name',
        description='Match against name using operator.',
        default=None,
    )
    order: str | None = Field(
        default=None, description='Field to sort by, defaults to ascending.'
    )
    per_page: int = Field(
        MIN_PER_PAGE,
        ge=MIN_PER_PAGE,
        le=MAX_PER_PAGE,
        description=f'Items per page (min {MIN_PER_PAGE}, max {MAX_PER_PAGE})',
    )
    page: int | None = Field(
        default=None,
        description='Page number to retrieve.',
    )

    @field_validator('per_page')
    @classmethod
    def limit_per_page(cls, value: int) -> int:
        """Limits the number of items per page.

        :param value: The number of items per page.
        :type value: int
        :returns: The limited number of items per page.
        :rtype: int
        """
        return MAX_PER_PAGE if value >= MAX_PER_PAGE else MIN_PER_PAGE

    @field_validator('page')
    @classmethod
    def offset(cls, value: int | None, values: ValidationInfo) -> int | None:
        """Calculates the offset for pagination.

        :param value: The page number.
        :type value: int | None
        :param values: The validation info.
        :type values: ValidationInfo
        :returns: The offset for pagination.
        :rtype: int | None
        """
        return (value - 1) * int(values.data['per_page']) if value else None


class CategoryQuery(BaseQuery):
    """Query model for categories."""

    pass


class BudgetQuery(BaseQuery):
    """Query model for budgets."""

    category_id: str | None = Field(
        default=None,
        description="The ID of the budget's category.",
    )
    user_id: str | None = Field(
        default=None,
        description="The ID of the budget's user.",
    )


class UserQuery(BaseQuery):
    """Query model for users."""

    pass
