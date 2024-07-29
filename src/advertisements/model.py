from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship

from ..base import OrmBase

from datetime import datetime

class Advertisement(OrmBase):
    __tablename__ = 'Advertisements'
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('Services.id'))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    photos = Column(JSON)
    is_vip = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    expired_at = Column(DateTime)

    service = relationship('Services', back_populates='advertisements')