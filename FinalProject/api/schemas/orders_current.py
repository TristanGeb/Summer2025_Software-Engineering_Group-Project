from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from api.models.orders import Orders


class OrderCurrentBase(BaseModel):
    order_history : Orders = None
    
class OrderCurrentCreate(OrderCurrentBase):
    order_id: int

class OrderCurrentUpdate(BaseModel):
    order_id: int

class OrderCurrent(OrderCurrentBase):
    id: int
    order_id: int
    
    class Config:
        from_attributes = True