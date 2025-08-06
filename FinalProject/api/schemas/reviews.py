from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.accounts import Accounts
class ReviewBase(BaseModel):
    name : str
    date : datetime
    body: str
    rating: int
    account: int
    
class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    body: Optional[str] = None
    rating: Optional[int] = None
    account: Optional[int] = None

class Review(ReviewBase):
    id: int
    
    class Config:
        from_attributes = True