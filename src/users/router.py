from fastapi import APIRouter, Depends

from .schema import UserCreate, ResponseUser
from .service import UserService, get_user_service

from typing import Optional, List

user_router = APIRouter(prefix="/api/v1/users", tags=["Пользователи"])

@user_router.get("/{user_id}", response_model=ResponseUser)
async def get_user(
    user_id: int, 
    service_sql: UserService = Depends(get_user_service)
):
    return await service_sql.get_one(user_id)

@user_router.post("/", response_model=ResponseUser)
async def post_user(
    user: UserCreate, 
    service_sql: UserService = Depends(get_user_service)
):
    return await service_sql.create(user)


@user_router.delete("/{category_id}", response_model=ResponseUser)
async def delete_user(
    user_id: int, 
    service_sql: UserService = Depends(get_user_service)
):
    return await service_sql.delete(user_id)