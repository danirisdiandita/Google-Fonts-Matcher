from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .common import Config 
import os

###
# Database Configuration
###
config = Config() 

SQLALCHEMY_DATABASE_URL = config.database_url #  "postgresql://tinnova:tinnova123@localhost/tinnova"
print("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    os.getenv("DB_URL", SQLALCHEMY_DATABASE_URL)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()