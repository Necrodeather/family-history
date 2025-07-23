from pydantic import UUID4, BaseModel, EmailStr

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


class UserQuery(BaseModel):
    name__like: str | None = None
    page: int | None = None
    order: str | None = None
