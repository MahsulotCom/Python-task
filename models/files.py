from operator import and_

from sqlalchemy import Column, Integer, String, Boolean, Float, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import URLType
from db import Base
from models.shop import Shop


class Files(Base):
    __tablename__ = "Files"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    source_id = Column(Integer, nullable=True)
    source = Column(String(30), nullable=True)
    image_url = Column(URLType, nullable=True)
    user_id = Column(Integer, nullable=False)

    shop = relationship('Shop', foreign_keys=[source_id],
                        backref=backref('shop_image', order_by="desc(Files.id)"),
                        primaryjoin=lambda: and_(Shop.id == Files.source_id, Files.source == "shop"))
