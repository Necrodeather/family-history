from pydantic import UUID4, BaseModel, EmailStr, field_validator

from domain.entities.base import BaseEntity


class Token(BaseModel):
    payload: str
    expire: int


class JWTToken(BaseModel):
    access_token: Token
    refresh_token: Token | None = None
    token_type: str = 'bearer'


class JWTUser(BaseEntity):
    id: str
    email: str

    @field_validator('id', mode='before')
    @classmethod
    def convert_uuid_to_str(cls, user_id: str | UUID4) -> str:
        if isinstance(user_id, str):
            return user_id
        return str(user_id)


class LoginUser(BaseModel):
    email: EmailStr
    password: str
