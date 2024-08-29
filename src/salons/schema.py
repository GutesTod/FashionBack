from pydantic import BaseModel, Field

from typing import Optional

class SalonBase(BaseModel):
    id: int
    name: str
    address: str
    contact_info: str

    class Config:
        orm_mode = True

class SalonCreate(SalonBase):
    user_id: int

class SalonUpdate(SalonBase):
    name: Optional[str]
    address: Optional[str]
    contact_info: Optional[str]

class SalonResponse(SalonBase):
    user_id: int