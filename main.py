import uvicorn

from app.core.config import app_settings


def main() -> None:
    uvicorn.run(
        app='app.public.api.app:app',
        host=app_settings.host,
        port=app_settings.port,
        reload=app_settings.debug_reload,
        workers=app_settings.workers,
    )


if __name__ == '__main__':
    main()
