from sqlalchemy import Column, Integer, String

from ..base import OrmBase

class Category(OrmBase):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)