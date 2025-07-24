from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from api.models.orders_all import OrderHistory


class OrderCurrentBase(BaseModel):
    order_history : OrderHistory = None
    
class OrderCurrentCreate(OrderCurrentBase):
    order_id: int

class OrderCurrentUpdate(BaseModel):
    order_id: int

class OrderCurrent(OrderCurrentBase):
    temp_id: int
    order_id: int
    
    class Config:
        from_attributes = True