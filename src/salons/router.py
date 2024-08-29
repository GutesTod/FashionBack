from fastapi import APIRouter, Depends

from .schema import SalonCreate, SalonResponse
from .service import SalonService, get_salon_service

from typing import Optional, List

salon_router = APIRouter(prefix="/api/v1/salons", tags=["Салоны"])

@salon_router.get("/get_salons/{limit}", response_model=List[SalonResponse])
async def get_salons(
    limit: Optional[int], 
    service: SalonService = Depends(get_salon_service)
):
    return await service.get_list(limit)

@salon_router.get("/get_salon/{user_id}")
async def get_salon(
    user_id: int,
    service: SalonService = Depends(get_salon_service)
):
    return await service.get_one(user_id)

@salon_router.post("/", response_model=SalonResponse)
async def post_salon(
    category: SalonCreate, 
    service: SalonService = Depends(get_salon_service)
):
    return await service.create(category)


@salon_router.delete("/{category_id}", response_model=SalonResponse)
async def delete_salon(
    salon_id: int, 
    service: SalonService = Depends(get_salon_service)
):
    await service.delete(salon_id)
    return {'id': salon_id}