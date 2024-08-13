from pydantic import BaseModel, Field
from datetime import date

from typing import Optional

class AdvertisementBase(BaseModel):
    salon_id: int = Field(..., description="Идентификатор салона")
    service_id: int = Field(..., description="Идентификатор услуги")
    title: str = Field(..., description="Заголовок объявления")
    description: str = Field(..., description="Описание объявления")
    price: float = Field(..., description="Цена")
    location: str = Field(..., description="Местоположение")
    type: str = Field(..., description="Тип оказания услуги")
    status: str = Field(..., description="Статус объявления")
    vip_status: bool = Field(..., description="VIP статус")
    start_date: date = Field(..., description="Дата начала")
    end_date: date = Field(..., description="Дата окончания")
    image_url: str = Field(..., description="URL изображения")

class AdvertisementCreate(AdvertisementBase):
    pass

class AdvertisementUpdate(AdvertisementBase):
    title: Optional[str] = Field(..., description="Заголовок объявления")
    description: Optional[str] = Field(..., description="Описание объявления")
    price: Optional[float] = Field(..., description="Цена")
    location: Optional[str] = Field(..., description="Местоположение")
    type: Optional[str] = Field(..., description="Тип оказания услуги")
    status: Optional[str] = Field(..., description="Статус объявления")
    vip_status: Optional[bool] = Field(..., description="VIP статус")
    start_date: Optional[date] = Field(..., description="Дата начала")
    end_date: Optional[date] = Field(..., description="Дата окончания")
    image_url: Optional[str] = Field(..., description="URL изображения")

class AdvertisementInDBBase(AdvertisementBase):
    ad_id: int = Field(..., description="Уникальный идентификатор объявления")

    class Config:
        orm_mode = True

class Advertisement(AdvertisementInDBBase):
    pass