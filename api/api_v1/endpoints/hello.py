from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from api.deps import get_db

router = APIRouter()

@router.get("", status_code=200)
async def hello():
    return "Welcome to the products api"