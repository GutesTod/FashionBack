from sqlalchemy import Column, Integer, String
from ..base import OrmBase

class User(OrmBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String)  # 'client', 'admin', 'salon_admin'
    contact_info = Column(String)
    telegram_id = Column(Integer, unique=True, index=True)