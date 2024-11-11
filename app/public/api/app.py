from fastapi import FastAPI

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
    return app


app = create_app()
