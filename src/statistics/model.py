from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship

from ..base import OrmBase

class Statistic(OrmBase):
    __tablename__ = 'Statistics'
    stat_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    action = Column(String)
    date = Column(TIMESTAMP)
    details = Column(Text)
    
    user = relationship('Users', back_populates='statistics')