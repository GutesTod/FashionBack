from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Salon(OrmBase):
    __tablename__ = 'Salons'
    salon_id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(Text)
    address = Column(String)
    payment_info = Column(Text)
    
    advertisements = relationship('Advertisements', back_populates='salon')
    payments = relationship('Payments', back_populates='salon')