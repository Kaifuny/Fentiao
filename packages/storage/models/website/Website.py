from Base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class WebSite(Base):
  __tablename__ = 'website'
  id = Column(Integer, primary_key=True, comment='Primary Key')
  name = Column(String(255), nullable=False, comment='Website Name')
  url = Column(String(255), nullable=False, comment='Website URL')
  localization = Column(String(255), comment='Localization')
  description = Column(Text)
  created = Column(DateTime, default=datetime.now)
  updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)