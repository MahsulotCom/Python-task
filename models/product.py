from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, DECIMAL, Text
from sqlalchemy.orm import relationship

from db import Base


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    unit = Column(String(30), nullable=False)
    category = Column(Integer,ForeignKey("Category.id"), nullable=False)
    real_price = Column(DECIMAL, nullable=False)
    trade_price = Column(DECIMAL, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer,ForeignKey('Users.id'))
