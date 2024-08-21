from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from ..base import OrmBase

from ..salons.model import Salon

class Service(OrmBase):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(DECIMAL)
    salon_id = Column(Integer, ForeignKey('salons.id'))
    salon = relationship('Salon', backref='services')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', backref='services')