from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from core.config import redis_settings


@asynccontextmanager
async def initial_fastapi_cache(_: FastAPI) -> AsyncIterator[None]:
    """Initializes the cache for the FastAPI application.

    :param _: The FastAPI application.
    :type _: FastAPI
    """
    redis = aioredis.from_url(redis_settings.uri)
    FastAPICache.init(RedisBackend(redis), prefix='backend-cache')
    yield
