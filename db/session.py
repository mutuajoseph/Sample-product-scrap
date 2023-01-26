from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import settings
from settings.config import settings

"""
To start talking to our database, the ORM's handle to the database is the Session
"""
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
conn = SessionLocal()