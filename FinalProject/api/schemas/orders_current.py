from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from api.models.orders import Orders
from enum import Enum

class OrderStatus(str, Enum):
    pending = "Pending"
    preparing = "Preparing"
    ready = "Ready"
    completed = "Completed"
    cancelled = "Cancelled"

class UpdateStatus(BaseModel):
    status: OrderStatus

class OrderStatusResponse(BaseModel):
    order_id: int
    status: OrderStatus

class OrderCurrentBase(BaseModel):
    pass
class OrderCurrentCreate(OrderCurrentBase):
    order_id: int

class OrderCurrentUpdate(BaseModel):
    order_id: int

class OrderCurrent(OrderCurrentBase):
    id: int
    order_id: int
    
    class Config:
        from_attributes = True