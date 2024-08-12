from ..base import OrmBase
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class User(OrmBase):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    role = Column(String)
    contact_info = Column(Text)
    
    bookings = relationship('Bookings', back_populates='user')
    notifications = relationship('Notifications', back_populates='user')
    statistics = relationship('Statistics', back_populates='user')