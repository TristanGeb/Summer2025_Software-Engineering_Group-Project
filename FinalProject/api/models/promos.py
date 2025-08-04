from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date 
from ..dependencies.database import Base

class PromoCodes(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    expiry_date = Column(Date, nullable=False, default=date.today)
    
    
    
    
    
    
    

    

