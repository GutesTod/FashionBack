from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from datetime import datetime

from ..base import OrmBase

class Category(OrmBase):
    __tablename__ = 'Сategories'
    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    
    services = relationship('Services', back_populates='category')