from Base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Platform(Base):
  __tablename__ = 'platform'
  id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)
  description = Column(Text)
  created = Column(DateTime, default=datetime.now)
  updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)