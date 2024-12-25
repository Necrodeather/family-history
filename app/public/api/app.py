from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.domain.exceptions import (
    CredentialsError,
    IncorrectLoginError,
    NotFoundError,
)
from app.public.api.v1 import api_router
from app.utils import read_pyproject_toml

project_info = read_pyproject_toml()


def create_app() -> FastAPI:
    app = FastAPI(
        title=project_info['project']['name'],
        version=project_info['project']['version'],
        description=project_info['project']['description'],
        license_info={'name': project_info['project']['license']},
    )
    app.include_router(api_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return app


app = create_app()


@app.exception_handler(CredentialsError)
async def credentials_error_handler(
    request: Request,
    exc: CredentialsError,
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
        headers={'WWW-Authenticate': 'Bearer'},
    )


@app.exception_handler(IncorrectLoginError)
async def incorrect_login_error_handler(
    request: Request,
    exc: IncorrectLoginError,
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={'message': exc.message},
    )


@app.exception_handler(NotFoundError)
async def not_found_handler(
    request: Request,
    exc: NotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={'message': exc.message},
    )
