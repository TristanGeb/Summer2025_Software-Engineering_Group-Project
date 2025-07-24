from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Tickets(Base):
    __tablename__ = "tickets"
   
    tix_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    