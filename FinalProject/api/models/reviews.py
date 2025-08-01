from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Reviews(Base):
    __tablename__ = "reviews"
    #added ID for parsing
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    date = Column(Date, nullable=False, default=date.today)
    body = Column(String(256),nullable = False)
    rating = Column(Integer, nullable=False)