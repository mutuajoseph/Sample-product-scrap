import secrets
from typing import List, Optional, Any, Union
from pydantic import BaseSettings,AnyHttpUrl,EmailStr,HttpUrl,PostgresDsn, validator

class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SECRET_KEY: str = secrets.token_urlsafe(32)

    FIRST_SUPERUSER_FIRST_NAME: Optional[str]
    FIRST_SUPERUSER_LAST_NAME: Optional[str]
    FIRST_SUPERUSER_EMAIL: Optional[str]
    FIRST_SUPERUSER_PASSWORD: Optional[str]

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]

    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int]
    ALGORITHM: Optional[str]

    ROLES_OPEN_REGISTRATION: Optional[bool]

    # DOS
    DOS_ACCESS_ID : Optional[str]
    DOS_SECRET_KEY :  Optional[str]
    DOS_ENDPOINT_URL : Optional[str]
    DOS_BUCKET_URL: Optional[str]
    DOS_REGION_NAME : Optional[str]
    DOS_CURRENT_UPLOAD_FOLDER: Optional[str]
    DOS_NAME_OF_BUCKET: Optional[str]

    class Config:
        env_file = ".env"

settings = Settings()