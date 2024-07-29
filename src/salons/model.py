from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from ..base_classes import OrmBase

class Salon(OrmBase):
    __tablename__ = 'Salons'
    salon_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    owner_id = Column(Integer, ForeignKey('Users.user_id'))
    subscription_type = Column(String(50))
    subscription_end_date = Column(Date)

    owner = relationship('Users', back_populates='salons')
    services = relationship('Services', back_populates='salon')