from typing import Self, Type

from pydantic import UUID4, BaseModel, EmailStr, Field, model_validator

from .base import BaseEntity


class UserCreate(BaseModel):
    """Represents a user to be created."""

    first_name: str = Field(description="The user's first name")
    last_name: str = Field(description="The user's last name")
    email: EmailStr = Field(description="The user's email address")
    password: str = Field(description="The user's password")


class UserUpdate(BaseModel):
    """Represents a user to be updated."""

    first_name: str | None = Field(
        default=None,
        description="The user's first name",
    )
    last_name: str | None = Field(
        default=None,
        description="The user's last name",
    )
    email: EmailStr | None = Field(
        default=None,
        description="The user's email address",
    )
    password: str | None = Field(
        default=None,
        description="The user's password",
    )


class UserRead(BaseEntity):
    """Represents a user that has been read from the database."""

    id: UUID4 = Field(description="The user's unique identifier")
    first_name: str = Field(description="The user's first name")
    last_name: str = Field(description="The user's last name")
    email: EmailStr = Field(description="The user's email address")


class UserRelation(BaseEntity):
    """Represents a relation to a user."""

    name: str = Field(default=None, description="The relation's name")

    @model_validator(mode='before')
    @classmethod
    def combine_fields(cls, data: Type[BaseModel]) -> Type[Self]:
        """Combines the first and last name to create the full name.

        :param data: The model data.
        :type data: Type[BaseModel]
        :returns: The model with the full name.
        :rtype: Type[Self]
        """
        cls.name = f'{data.first_name} {data.last_name}'
        return cls
