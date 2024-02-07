import mysql.connector

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db1",
)

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/db2"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()