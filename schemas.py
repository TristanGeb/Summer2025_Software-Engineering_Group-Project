from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class GuestOrderCreate(BaseModel):
    name: str
    phone: str
    address: str
    order_items: str
    order_type: str

class GuestOrderOut(BaseModel):
    tracking_number: str
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    address: Optional[str]

class PromoCreate(BaseModel):
    code: str
    discount: float
    expiry_date: date

class PromoApply(BaseModel):
    promo_code: str
    order_total: float

class PromoOut(BaseModel):
    code: str
    discount: float
    expiry_date: date
    class Config:
        orm_mode = True