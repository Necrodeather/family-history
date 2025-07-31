import uvicorn

from containers.root import AppContainer
from core.config import app_settings, database_settings
from public.api.app import create_app
from public.api.lifespan import initial_fastapi_cache

container = AppContainer()
container.database_config.from_pydantic(database_settings)
app = create_app(container=container, lifespan=initial_fastapi_cache)


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=app_settings.host,
        port=app_settings.port,
        reload=app_settings.debug_reload,
        workers=app_settings.workers,
    )
