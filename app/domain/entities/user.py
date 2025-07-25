from typing import Self, Type

from pydantic import UUID4, BaseModel, EmailStr, model_validator

from .base import BaseEntity


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserRead(BaseEntity):
    id: UUID4
    first_name: str
    last_name: str
    email: EmailStr


class UserRelation(BaseEntity):
    name: str

    @model_validator(mode='before')
    @classmethod
    def combine_fields(cls, data: Type[BaseModel]) -> Type[Self]:
        cls.name = f'{data.first_name} {data.last_name}'
        return cls
