from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, DECIMAL, Text,Boolean
from sqlalchemy.orm import relationship

from db import Base


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    unit = Column(String(30), nullable=False)
    category_id = Column(Integer,ForeignKey("Category.id"), nullable=False)
    real_price = Column(Integer, nullable=False)
    trade_price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    active = Column(Boolean, default=True,nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer,ForeignKey('Users.id'))
