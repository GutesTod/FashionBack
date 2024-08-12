from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Booking(OrmBase):
    __tablename__ = 'Bookings'
    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    ad_id = Column(Integer, ForeignKey('Advertisements.ad_id'))
    datetime = Column(DateTime)
    status = Column(String)

    user = relationship('Users', back_populates='bookings')
    advertisement = relationship('Advertisements', back_populates='bookings')
