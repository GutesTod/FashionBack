from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import OrmBase

class Booking(OrmBase):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='bookings')
    service_id = Column(Integer, ForeignKey('services.id'))
    service = relationship('Service', backref='bookings')
    booking_date = Column(DateTime)
    status = Column(String)  # 'pending', 'confirmed', 'canceled'
