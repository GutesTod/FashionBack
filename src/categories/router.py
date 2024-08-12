from fastapi import APIRouter, Depends

from .schema import CategoryBase, CategoryCreate
from .service import CategoryService, get_category_service

from typing import Optional

category_router = APIRouter(prefix="/api/v1/categories", tags=["Категории"])

@category_router.get("/{limit}", response_model=CategoryBase)
async def get_categories(
    limit: Optional[int], 
    service: CategoryService = Depends(get_category_service)
):
    return service.get_list(limit)

@category_router.post("/", response_model=CategoryBase)
async def post_category(
    category: CategoryCreate, 
    service: CategoryService = Depends(get_category_service)
):
    return service.create(category)


@category_router.delete("/{category_id}", response_model=CategoryBase)
async def delete_category(
    category_id: int, 
    service: CategoryService = Depends(get_category_service)
):
    return service.create(category_id)