from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItems(Base):
    __tablename__ = "menu_items"
    
    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    price = Column(DECIMAL(10, 2), nullable=False)
    food_category = Column(String(256),nullable = False)
    calories = Column(Integer,nullable=False)

    
    related_menus= Column(Integer, ForeignKey("menus.id"))
    


