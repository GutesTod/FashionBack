from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import OrmBase

from ..users.model import User

class Salon(OrmBase):
    __tablename__ = 'salons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    contact_info = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='salons')