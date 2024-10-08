from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship

from datetime import datetime

from ..base import OrmBase

class Review(OrmBase):
    __tablename__ = 'Reviews'
    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('Bookings.id'))
    rating = Column(Integer)
    comment = Column(Text)
    reviewed_at = Column(DateTime, default=datetime.now)

    booking = relationship('Bookings', back_populates='review')