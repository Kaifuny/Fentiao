from Base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Account(Base):
  __tablename__ = 'account'
  id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False, comment='Username')
  password = Column(String(255), nullable=False, comment='Password')
  email = Column(String(255), nullable=False, comment='Email')
  phone = Column(String(255), nullable=False, comment='Phone')
  type = Column(String(255), nullable=False, comment='Account Type')
  created = Column(DateTime, default=datetime.now)
  updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)