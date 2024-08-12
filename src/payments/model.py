from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Statistic(OrmBase):
    __tablename__ = 'Payments'
    payment_id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('salons.salon_id'))
    amount = Column(DECIMAL)
    payment_date = Column(Date)
    payment_method = Column(String)
    status = Column(String)
    
    salon = relationship('Salons', back_populates='payments')