from fastapi import Request
from fastapi.responses import JSONResponse

from domain.exceptions import (
    CredentialsError,
    EntityAlreadyError,
    IncorrectLoginError,
    NotFoundError,
    UserAlreadyRegisteredError,
)


async def credentials_error(
    request: Request,
    exc: CredentialsError,
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
        headers={'WWW-Authenticate': 'Bearer'},
    )


async def incorrect_login_error(
    request: Request,
    exc: IncorrectLoginError,
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
    )


async def not_found(
    request: Request,
    exc: NotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={'message': exc.message},
    )


async def user_already_registered(
    request: Request,
    exc: UserAlreadyRegisteredError,
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={'message': exc.message},
    )


async def entity_already(
    request: Request,
    exc: EntityAlreadyError,
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={'message': exc.message},
    )


error_handlers = [
    not_found,  # 404
    credentials_error,  # 401
    incorrect_login_error,  # 401
    user_already_registered,  # 409
    entity_already,  # 409
]
