from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import OrmBase

class Subscription(OrmBase):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    salon_id = Column(Integer, ForeignKey('salons.id'))
    salon = relationship('Salon', backref='subscriptions')
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    plan = Column(String)  # 'standard', 'vip'