from fastapi import APIRouter

from api.api_v1.endpoints import (hello, products, search)

# router instance
api_router = APIRouter()

api_router.include_router(hello.router, prefix="/welcome", tags=["API WELCOME MESSAGE"])
api_router.include_router(products.router, prefix="/products", tags=["PRODUCT OPERATIONS"])
api_router.include_router(search.router, prefix="/search", tags=["SEARCH OPERATIONS"])