from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderHistoryBase(BaseModel):
    name : str
    date : datetime
    total: int
    
class OrderHistoryCreate(OrderHistoryBase):
    pass

class OrderHistoryUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    total:Optional[int] = None

class OrderHistory(OrderHistoryBase):
    id: int
    
    class Config:
        from_attributes = True