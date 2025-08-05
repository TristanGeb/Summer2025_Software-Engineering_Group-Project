from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItems(Base):
    __tablename__ = "menu_items"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    price = Column(DECIMAL(10, 2), nullable=False)
    food_category = Column(String(256),nullable = False)
    calories = Column(Integer,nullable=False)
    #add links to resources for ingredents
    #TODO: implement related menus
    #related_menus= Column(Integer, ForeignKey("menus.menu_id"))

def compare(self, comp):
    if "id" in comp:
        if self.id != comp["id"]:
            return False
    if "name" in comp:
        if self.name != comp["name"]:
            return False
    if "price" in comp:
        if self.price != comp["price"]:
            return False
    if "food_category" in comp:
        if self.food_category != comp["food_category"]:
            return False
    if "calories" in comp:
        if self.calories != comp["calories"]:
            return False
    return True

