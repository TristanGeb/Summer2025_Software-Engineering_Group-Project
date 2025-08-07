from pydantic import BaseModel
from typing import List, Optional


class MenuItemBase(BaseModel):
    name : str
    price : float
    food_category: str
    calories: int
    menu_id:int
class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    food_category: Optional[str] = None
    calories: Optional[int] = None
    menu_id: Optional[int] = None
class MenuItem(MenuItemBase):
    id: int
    
    class Config:
        from_attributes = True