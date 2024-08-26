from pydantic import BaseModel, Field

from .model import ServiceLocation

class ServiceBase(BaseModel):
    name: str
    description: str
    min_price: float
    max_price: float
    duration: int
    salon_id: int
    category_id: int
    service_location: ServiceLocation

    class Config:
        orm_mode = True

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    id: int

class ServiceResponse(ServiceBase):
    id: int