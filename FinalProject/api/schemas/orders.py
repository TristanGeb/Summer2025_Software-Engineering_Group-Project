from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    name : str
    date : datetime
    total: int
    
class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    total:Optional[int] = None

class Order(OrderBase):
    id: int
    
    class Config:
        from_attributes = True