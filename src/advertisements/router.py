from fastapi import APIRouter, Depends

from .schema import Advertisement, AdvertisementCreate, AdvertisementUpdate
from .service import AdvertisementsService, get_advertisements_service

from typing import Optional, List

category_router = APIRouter(prefix="/api/v1/advertisements", tags=["Объявления"])

@category_router.get("/{limit}", response_model=List[Advertisement])
async def get_advertisements(
    limit: Optional[int], 
    service: AdvertisementsService = Depends(get_advertisements_service)
):
    return service.get_list(limit)

@category_router.post("/", response_model=Advertisement)
async def post_advertisement(
    advertisement: AdvertisementCreate, 
    service: AdvertisementsService = Depends(get_advertisements_service)
):
    return service.create(advertisement)


@category_router.delete("/{advertisement_id}", response_model=Advertisement)
async def delete_advertisement(
    advertisement_id: int, 
    service: AdvertisementsService = Depends(get_advertisements_service)
):
    return service.delete(advertisement_id)

@category_router.put("/{advertisement_id}", response_model=Advertisement)
async def update_advertisement(
    advertisement_id: int, 
    update_data: AdvertisementUpdate,
    service: AdvertisementsService = Depends(get_advertisements_service)
):
    return service.update(update_data, advertisement_id)