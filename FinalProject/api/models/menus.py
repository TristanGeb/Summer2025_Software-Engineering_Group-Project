from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menus"
    
    menu_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_name = Column(String(256),nullable = False)
