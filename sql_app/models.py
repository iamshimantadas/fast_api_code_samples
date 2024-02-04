from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, Text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ ="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    phone = Column(BigInteger, nullable=True)
    password = Column(String(250))
    

class Blogs(Base):
    __tablename__ = "blogs"
    blogid = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(200))
    description = Column(Text)    