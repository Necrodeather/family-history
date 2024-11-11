from fastapi import APIRouter

from app.public.api.v1.auth import auth_router
from app.public.api.v1.expenses import expenses_router
from app.public.api.v1.expenses_category import expenses_category_router
from app.public.api.v1.income import income_router
from app.public.api.v1.incomes_category import incomes_category_router
from app.public.api.v1.user import user_router

budget_router = APIRouter(prefix='/budget')
budget_router.include_router(
    expenses_category_router,
    tags=['expenses_category'],
)
budget_router.include_router(
    incomes_category_router,
    tags=['incomes_category'],
)
budget_router.include_router(income_router, tags=['income'])
budget_router.include_router(expenses_router, tags=['expenses'])

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(auth_router, tags=['auth'])
api_router.include_router(budget_router)
api_router.include_router(user_router, tags=['user'])
