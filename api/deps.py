from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from settings.config import settings
from db.session import SessionLocal
import schemas, utils

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



