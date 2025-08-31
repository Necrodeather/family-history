from pydantic import UUID4, BaseModel, EmailStr, field_validator

from domain.entities.base import BaseEntity


class Token(BaseModel):
    """Represents a token with its payload and expiration time."""

    payload: str
    expire: int


class JWTToken(BaseModel):
    """Represents a JWT token, including access and refresh tokens."""

    access_token: Token
    refresh_token: Token | None = None
    token_type: str = 'bearer'


class JWTUser(BaseEntity):
    """Represents a user authenticated via JWT."""

    id: str
    email: str

    @field_validator('id', mode='before')
    @classmethod
    def convert_uuid_to_str(cls, user_id: str | UUID4) -> str:
        """Converts a UUID to a string.

        :param user_id: The user ID to convert.
        :type user_id: str | UUID4
        :returns: The user ID as a string.
        :rtype: str
        """
        if isinstance(user_id, str):
            return user_id
        return str(user_id)


class LoginUser(BaseModel):
    """Represents a user logging in."""

    email: EmailStr
    password: str
