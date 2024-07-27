from Base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)