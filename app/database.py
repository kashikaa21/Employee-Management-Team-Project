<<<<<<< HEAD
from sqlalchemy import text , create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
import os

from urllib.parse import quote_plus

load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(
    DATABASE_URL,
)
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "mysql+pymysql://root:Coforge%40123456@localhost:3306/employee_db"

engine = create_engine(db_url)
>>>>>>> origin/salary

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
<<<<<<< HEAD

=======
>>>>>>> origin/salary
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()