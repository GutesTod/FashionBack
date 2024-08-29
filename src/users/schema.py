from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    username: str
    role: str
    contact_info: str

class UserUpdate(UserBase):
    username: Optional[str]
    role: Optional[str]
    contact_info: Optional[str]

class ResponseUser(UserBase):
    username: str
    role: str
    contact_info: str