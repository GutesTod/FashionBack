from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DECIMAL, Date
from sqlalchemy.orm import relationship

from ..base import OrmBase

from datetime import datetime

class Advertisement(OrmBase):
    __tablename__ = 'Advertisements'
    ad_id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('Salons.salon_id'))
    service_id = Column(Integer, ForeignKey('Services.service_id'))
    title = Column(String)
    description = Column(Text)
    price = Column(DECIMAL)
    location = Column(String)
    type = Column(String)
    status = Column(String)
    vip_status = Column(Boolean)
    start_date = Column(Date)
    end_date = Column(Date)
    image_url = Column(String)

    salon = relationship('Salons', back_populates='advertisements')
    service = relationship('Services', back_populates='advertisements')