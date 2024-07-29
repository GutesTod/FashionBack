from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, Text
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Service(OrmBase):
    __tablename__ = 'Services'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    category = Column(Enum('category1', 'category2', 'category3'))  # Замените на ваши категории
    price = Column(DECIMAL(10, 2))
    salon_id = Column(Integer, ForeignKey('Salons.id'))

    salon = relationship('Salons', back_populates='services')
    advertisements = relationship('Advertisements', back_populates='service')
    bookings = relationship('Bookings', back_populates='service')