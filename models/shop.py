from sqlalchemy import Column, Integer, String, DateTime, Text, func,ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Shop(Base):
    __tablename__ = "Shop"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer,ForeignKey('Users.id'))

