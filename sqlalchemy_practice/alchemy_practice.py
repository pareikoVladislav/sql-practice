import json
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    or_
)
from sqlalchemy.orm import sessionmaker, declarative_base

db_path = 'sqlite:///example.db'
engine = create_engine(db_path)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(25), nullable=True)
    age = Column(Integer)
    email = Column(String(50), unique=True)
    phone = Column(String(30), unique=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)


Base.metadata.create_all(engine)
