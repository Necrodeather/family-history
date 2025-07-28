import uvicorn

from core.config import app_settings
from public.api.app import create_app

app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=app_settings.host,
        port=app_settings.port,
        reload=app_settings.debug_reload,
        workers=app_settings.workers,
    )
