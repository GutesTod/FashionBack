from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from datetime import datetime

from ..base import OrmBase

class Notification(OrmBase):
    __tablename__ = 'Notifications'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    message = Column(Text)
    sent_at = Column(DateTime, default=datetime.now)
    is_read = Column(Boolean, default=False)

    user = relationship('Users', back_populates='notifications')