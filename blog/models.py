from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import Relationship

class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(50), nullable=False)
    content=Column(String(1000), nullable=False)
    user_id=Column(Integer, ForeignKey("users.id"))
    creator=Relationship("User", back_populates="blogs")

class User(Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(50), nullable=False)
    email=Column(String(100), nullable=False, unique=True)
    password=Column(String(100), nullable=False)
    blogs=Relationship("Blog", back_populates="creator")