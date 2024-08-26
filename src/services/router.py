from fastapi import APIRouter, Depends

from .schema import ServiceCreate, ServiceResponse
from .service import Service, get_service
from .model import ServiceLocation

from typing import Optional, List

service_router = APIRouter(prefix="/api/v1/services", tags=["Сервисы"])

@service_router.get("/{limit}", response_model=List[ServiceResponse])
async def get_categories(
    limit: Optional[int], 
    service_sql: Service = Depends(get_service)
):
    return await service_sql.get_list(limit)

@service_router.post("/", response_model=ServiceResponse)
async def post_category(
    service: ServiceCreate, 
    service_sql: Service = Depends(get_service)
):
    return await service_sql.create(service)


@service_router.delete("/{category_id}", response_model=ServiceResponse)
async def delete_category(
    category_id: int, 
    service_sql: Service = Depends(get_service)
):
    return await service_sql.delete(category_id)

@service_router.get("/enum/", response_model=list)
async def get_enum_locations():
    return [location.name for location in ServiceLocation]