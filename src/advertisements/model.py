from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from ..services.model import Service

from ..base import OrmBase

class Advertisement(OrmBase):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship('Service', backref='advertisements')
    is_vip = Column(Boolean, default=False)
    filters = Column(JSONB)  # Фильтры: местоположение, цена и т.д.