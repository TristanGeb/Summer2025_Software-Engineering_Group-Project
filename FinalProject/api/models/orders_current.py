from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class CurrentOrders(Base):
    __tablename__ = "orders_current"
    temp_id =  Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer,ForeignKey("orders_all.order_id"))
    order_history = relationship("OrderHistory",back_populates="orders_current")