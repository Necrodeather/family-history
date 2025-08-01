from typing import Any, Sequence

from dependency_injector.containers import DeclarativeContainer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from containers.root import AppContainer

from .error_handlers import error_handlers
from .utils import read_pyproject_toml
from .v1.routers import api_router


class Server:
    app: FastAPI = FastAPI

    def __init__(self, app: FastAPI, container: DeclarativeContainer) -> None:
        self.app = app
        self.app.container = container

        self._register_middleware(app)
        self._register_routers(app)
        self._base_information(app)
        self._register_exception_handlers(app, error_handlers)

    def get_app(self) -> FastAPI:
        return self.app

    @staticmethod
    def _base_information(app: FastAPI) -> None:
        if app.openapi_schema:
            return app.openapi_schema

        project_info = read_pyproject_toml()
        app.openapi_schema = get_openapi(
            title=project_info['project']['name'],
            version=project_info['project']['version'],
            description=project_info['project']['description'],
            license_info={'name': project_info['project']['license']},
            routes=app.routes,
        )

    @staticmethod
    def _register_middleware(app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )

    @staticmethod
    def _register_routers(app: FastAPI) -> None:
        app.include_router(api_router)

    @staticmethod
    def _register_exception_handlers(
        app: FastAPI,
        exception_handlers: Sequence[object],
    ) -> None:
        for handler in exception_handlers:
            app.add_exception_handler(handler.__annotations__['exc'], handler)


def create_app(
    container: AppContainer,
    *args: Any,
    **kwargs: Any,
) -> FastAPI:
    app = FastAPI(*args, **kwargs)
    return Server(app=app, container=container).get_app()
