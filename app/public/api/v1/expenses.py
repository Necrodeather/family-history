from uuid import UUID

from fastapi import APIRouter

from app.domain.entities.budget import BudgetCreateUpdateForm, BudgetRead
from app.service.budget import income_service

expenses_router = APIRouter(prefix='/expenses')


@expenses_router.get('/')
async def get_all() -> list[BudgetRead]:
    return await income_service.get_all()


@expenses_router.get('/{category_id}')
async def get_by_id(category_id: UUID) -> BudgetRead:
    return await income_service.get_by_id(category_id)


@expenses_router.post('/')
async def create(
    category: BudgetCreateUpdateForm,
) -> BudgetRead:
    return await income_service.create(category)


@expenses_router.put('/{category_id}')
async def update(
    category_id: UUID,
    category: BudgetCreateUpdateForm,
) -> BudgetRead:
    return await income_service.update_by_id(category_id, category)


@expenses_router.delete('/{category_id}')
async def delete(
    category_id: UUID,
) -> None:
    await income_service.delete_by_id(category_id)
