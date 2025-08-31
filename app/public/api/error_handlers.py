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
    """Handles the CredentialsError exception.

    :param request: The request that caused the exception.
    :type request: Request
    :param exc: The exception that was raised.
    :type exc: CredentialsError
    :returns: A JSON response with a 401 status code.
    :rtype: JSONResponse
    """
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
        headers={'WWW-Authenticate': 'Bearer'},
    )


async def incorrect_login_error(
    request: Request,
    exc: IncorrectLoginError,
) -> JSONResponse:
    """Handles the IncorrectLoginError exception.

    :param request: The request that caused the exception.
    :type request: Request
    :param exc: The exception that was raised.
    :type exc: IncorrectLoginError
    :returns: A JSON response with a 401 status code.
    :rtype: JSONResponse
    """
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
    )


async def not_found(
    request: Request,
    exc: NotFoundError,
) -> JSONResponse:
    """Handles the NotFoundError exception.

    :param request: The request that caused the exception.
    :type request: Request
    :param exc: The exception that was raised.
    :type exc: NotFoundError
    :returns: A JSON response with a 404 status code.
    :rtype: JSONResponse
    """
    return JSONResponse(
        status_code=404,
        content={'message': exc.message},
    )


async def user_already_registered(
    request: Request,
    exc: UserAlreadyRegisteredError,
) -> JSONResponse:
    """Handles the UserAlreadyRegisteredError exception.

    :param request: The request that caused the exception.
    :type request: Request
    :param exc: The exception that was raised.
    :type exc: UserAlreadyRegisteredError
    :returns: A JSON response with a 409 status code.
    :rtype: JSONResponse
    """
    return JSONResponse(
        status_code=409,
        content={'message': exc.message},
    )


async def entity_already(
    request: Request,
    exc: EntityAlreadyError,
) -> JSONResponse:
    """Handles the EntityAlreadyError exception.

    :param request: The request that caused the exception.
    :type request: Request
    :param exc: The exception that was raised.
    :type exc: EntityAlreadyError
    :returns: A JSON response with a 409 status code.
    :rtype: JSONResponse
    """
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
