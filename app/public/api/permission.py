from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError, decode, encode

from core.config import app_settings
from domain.entities.auth import JWTUser, Token
from domain.exceptions import CredentialsError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/auth/login')


def create_token(data: JWTUser, is_refreshed: bool = False) -> Token:
    to_encode = data.model_dump().copy()
    if is_refreshed:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=app_settings.refresh_token_expire_minutes
        )
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=app_settings.access_token_expire_minutes
        )
    encoded_jwt = encode(
        to_encode,
        app_settings.secret_key,
        algorithm=app_settings.algorithm,
    )
    return Token(payload=encoded_jwt, expire=int(expire.timestamp()))


async def decode_token(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> None:
    try:
        payload = decode(
            token,
            app_settings.secret_key,
            algorithms=[app_settings.algorithm],
        )
        if not payload:
            raise CredentialsError()
    except InvalidTokenError:
        raise CredentialsError()
    return JWTUser.model_validate(payload)
