from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .menuitems import MenuItems
class Menu(Base):
    __tablename__ = "menus"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_name = Column(String(256),nullable = False)

    items=relationship("MenuItems",back_populates="related_menu")
def compare(self, comp):
    if "id" in comp:
        if self.id != comp["id"]:
            return False
    if "menu_name" in comp:
        if self.menu_name != comp["menu_name"]:
            return False
    return True