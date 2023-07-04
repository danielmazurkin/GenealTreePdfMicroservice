from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()
app = FastAPI()

# Создаем базу данных SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

PATH_TO_PDF_WKHTML = os.getenv('PATH_TO_PDF', default='/usr/bin/wkhtmltopdf')
