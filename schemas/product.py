from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr

class ProductCreate(BaseModel):
    title: str
    description: str
    brand: Optional[bool]
    images_link: str
    upc: str
    department: str
    premium_brand: Optional[bool]
    rating: int
    ratings_total: int

class ProductUpdate(BaseModel):
    title: str
    description: str
    brand: str
    images_link: str
    upc: str
    department: str
    premium_brand: Optional[bool]
    rating: int
    ratings_total: int

class ProductInDB(ProductCreate):
    id: int
    public_id: str
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True
