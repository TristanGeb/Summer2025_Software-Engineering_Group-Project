from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderCurrentBase(BaseModel):
    name : str
    date : datetime
    total: int
    
class OrderCurrentCreate(OrderCurrentBase):
    pass

class OrderCurrentUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    total:Optional[int] = None

class OrderCurrent(OrderCurrentBase):
    order_id: int
    
    class Config:
        from_attributes = True