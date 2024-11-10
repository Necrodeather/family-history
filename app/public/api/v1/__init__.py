from fastapi import APIRouter

from app.public.api.v1.user import user_router
from app.public.api.v1.auth import auth_router
from app.public.api.v1.budget import budget_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(user_router, tags=["user"])
api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(budget_router, tags=["budget"])


__all__ = ["api_router"]
