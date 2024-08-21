from sqlalchemy import Column, Integer, DECIMAL, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import OrmBase

class Payment(OrmBase):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', backref='payments')
    amount = Column(DECIMAL)
    payment_date = Column(DateTime)
    payment_method = Column(String)