from fastapi import APIRouter, Depends

from .schema import Advertisement, AdvertisementCreate, AdvertisementUpdate
from .service import AdvertisementsService, get_advertisement_service

from typing import Optional, List

advertisement_router = APIRouter(prefix="/api/v1/advertisements", tags=["Объявления"])

@advertisement_router.get("/{limit}")
async def get_advertisements(
    limit: Optional[int], 
    service: AdvertisementsService = Depends(get_advertisement_service)
):
    return await service.get_list(limit)

@advertisement_router.post("/")
async def post_advertisement(
    advertisement: AdvertisementCreate, 
    service: AdvertisementsService = Depends(get_advertisement_service)
):
    return await service.create(advertisement)


@advertisement_router.delete("/{advertisement_id}")
async def delete_advertisement(
    advertisement_id: int, 
    service: AdvertisementsService = Depends(get_advertisement_service)
):
    return await service.delete(advertisement_id)

@advertisement_router.put("/{advertisement_id}")
async def update_advertisement(
    advertisement_id: int, 
    update_data: AdvertisementUpdate,
    service: AdvertisementsService = Depends(get_advertisement_service)
):
    return await service.update(update_data, advertisement_id)