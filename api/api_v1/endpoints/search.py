from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from api.deps import get_db
from schemas.product import ProductInDB
from models.products import Products

router = APIRouter()

@router.get("/search", status_code=200, response_model=List[ProductInDB])  
async def seach_for_a_product(title: Optional[str]=Query(None), db:Session = Depends(get_db)):
    query = []
    if title:
        query.append(Products.title.ilike('%'+title+'%'))  

    result = db.query(Products).filter(*query).all() 

    return result