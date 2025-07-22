from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReviewBase(BaseModel):
    name : str
    date : datetime
    body: str
    rating: int
    
class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime] = None
    body: Optional[str] = None
    rating: Optional[int] = None

class Review(ReviewBase):
    id: int
    
    class Config:
        from_attributes = True