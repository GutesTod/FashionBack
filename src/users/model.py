from ..base import OrmBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(OrmBase):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    salons = relationship('Salons', back_populates='owner')
    bookings = relationship('Bookings', back_populates='user')
    notifications = relationship('Notifications', back_populates='user')