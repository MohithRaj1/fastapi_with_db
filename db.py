from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
Base = declarative_base()

DATABASE_URL = os.getenv("DATABASES_URL")
print("DATABASE_URL",DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_arg={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=enine)
def get_db():
    db=create_session_local()
    try:
        yield db
    finally:
        db.close()