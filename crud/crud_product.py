from itertools import product
from crud.base import CRUDBase
from models.products import Products
from schemas.product import ProductCreate, ProductInDB, ProductUpdate

from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional, Any

class CRUDProduct(CRUDBase[Products, ProductCreate, ProductUpdate]):

    def get(self, db: Session) ->  Optional[Products]:
        return db.query(Products).all()

    def get_by_id(self, db: Session, id: int) -> Optional[Products]:
        return db.query(Products).filter(Products.id == id).first()

    def create(self, db: Session, *, obj_in: ProductCreate) -> Products:

        product_obj = Products(
            title = obj_in.title,
            description = obj_in.description,
            brand = obj_in.brand,
            images_link = obj_in.images_link,
            upc = obj_in.upc,
            department = obj_in.department,
            premium_brand = obj_in.premium_brand,
            rating = obj_in.rating,
            ratings_total = obj_in.ratings_total,
        )

        db.add(product_obj)
        db.commit()
        db.refresh(product_obj)
        return product_obj

product = CRUDProduct(Products)