from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class GuestOrder(Base):
    __tablename__ = "guest_orders"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    address = Column(String)
    order_items = Column(String)  # Comma-separated items or JSON string
    order_type = Column(String)
    tracking_number = Column(String, unique=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    address = Column(String)

class PromoCode(Base):
    __tablename__ = "promocodes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    discount = Column(Float)
    expiry_date = Column(Date)
    is_active = Column(Boolean, default=True)