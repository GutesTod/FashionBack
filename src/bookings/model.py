from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Booking(OrmBase):
    __tablename__ = 'Bookings'
    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    service_id = Column(Integer, ForeignKey('Services.service_id'))
    booking_date = Column(DateTime)
    status = Column(String(50))

    user = relationship('Users', back_populates='bookings')
    service = relationship('Services', back_populates='bookings')
    review = relationship('Reviews', back_populates='booking')
