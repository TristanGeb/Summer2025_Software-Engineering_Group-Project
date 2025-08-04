from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class PromosBase(BaseModel):
   expiry_date : datetime
    
class PromosCreate(PromosBase):
    pass

class PromosUpdate(BaseModel):
    expiry_date: Optional[datetime] = None

class Promos(PromosBase):
    id: int
    
    class Config:
        from_attributes = True