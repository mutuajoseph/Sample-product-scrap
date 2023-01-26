import uuid
from sqlalchemy import Boolean, DateTime, func, String, Integer, Column
from db.base_class import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    public_id = Column(String(length=256), unique=True, nullable=False, default=lambda: uuid.uuid4())
    title = Column(String(length=256), nullable=False)
    description = Column(String(length=256), nullable=False)
    brand = Column(String(length=256), nullable=False)
    images_link = Column(String(length=256), nullable=False)
    upc = Column(String(length=256), nullable=False)
    department = Column(String(length=256), nullable=False)
    premium_brand = Column(Boolean, nullable=False, default=False)
    rating = Column(Integer, nullable=False)
    ratings_total = Column(Integer, nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    update = Column(DateTime(timezone=True), onupdate=func.now())
