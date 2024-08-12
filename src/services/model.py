from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, Text
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Service(OrmBase):
    __tablename__ = 'services'
    service_id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    name = Column(String)
    description = Column(Text)
    
    category = relationship('Categories', back_populates='services')
    advertisements = relationship('Advertisements', back_populates='service')