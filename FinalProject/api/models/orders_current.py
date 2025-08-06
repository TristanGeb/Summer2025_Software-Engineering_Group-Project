import enum

from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date, Enum
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class OrderStatus(enum.Enum):
    pending = "Pending"
    preparing = "Preparing"
    ready = "Ready"
    completed = "Completed"
    cancelled = "Cancelled"

class CurrentOrders(Base):
    __tablename__ = "orders_current"
    temp_id =  Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer,ForeignKey("orders_all.order_id"))
    status = Column(Enum(OrderStatus), default = OrderStatus.pending, nullable = False)

    order_history = relationship("OrderHistory",back_populates="orders_current")