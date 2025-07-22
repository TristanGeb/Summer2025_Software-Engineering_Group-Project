from pydantic import BaseModel
from typing import Optional


class MenuBase(BaseModel):
    menu_name : str
    
class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    menu_name: Optional[str] = None
    

class Menu(MenuBase):
    menu_id: int
    
    class Config:
        from_attributes = True