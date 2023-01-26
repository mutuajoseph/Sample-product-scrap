from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List, Optional

from api.deps import get_db
from models.products import Products
from schemas.product import ProductCreate, ProductInDB
from crud.crud_product import product
from utils.digital_ocean_spaces import upload_to_spaces, delete_upload
from settings.config import settings

router = APIRouter()

@router.get("", status_code=200, response_model=List[ProductInDB])
async def get_all_products(db: Session = Depends(get_db)):
    return product.get(db=db)

@router.get("/{id}", status_code=200, response_model=ProductInDB)
async def get_a_single_product(id: int, db: Session = Depends(get_db)):
    product_item = product.get_by_id(id=id, db=db)

    if product_item is None:
        raise HTTPException(status_code=404, detail=f'product with id {id} was not found')

    return product_item  

@router.post("", status_code=201, response_model=ProductInDB)
async def add_new_product(
                    file: UploadFile, title: str = Form(),
                    description: str = Form(), brand: bool = Form(),
                    upc: str = Form(), department: str = Form(),
                    premium_brand: bool = Form(), rating: int = Form(),
                    ratings_total: int = Form(),
                    db: Session = Depends(get_db)
                    ):
    try:
        file_path = await upload_to_spaces(file=file)

        if file_path:
            file_link = f"{settings.DOS_BUCKET_URL}/{settings.DOS_CURRENT_UPLOAD_FOLDER}/{file.filename}"

            new_product = ProductCreate(
                title=title,
                description=description,
                brand=brand,
                upc=upc,
                department=department,
                premium_brand=premium_brand,
                rating=rating,
                ratings_total=ratings_total,
                images_link=file_link
            )

            print(new_product)
            created_product = product.create(db=db, obj_in=new_product)
            delete_upload(filename=file.filename)
            return created_product

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')  
