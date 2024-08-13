from pydantic import BaseModel, Field
from datetime import datetime

class NotificationBase(BaseModel):
    title: str
    message: str
    user_id: int
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(BaseModel):
    title: str = None
    message: str = None
    is_read: bool = None

class NotificationInDBBase(NotificationBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

class Notification(NotificationInDBBase):
    pass

class NotificationInDB(NotificationInDBBase):
    pass