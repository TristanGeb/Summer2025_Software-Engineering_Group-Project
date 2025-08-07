import enum
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date,Enum
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
    id =  Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer,ForeignKey("all_orders.id"))
    status = Column(Enum(OrderStatus), default = OrderStatus.pending, nullable = False)

    order = relationship("Orders")
    #TODO: what does back_populates actually do
    #TODO: is it Orders or Order and what exactly is it pointing to


def compare(self, comp):
    if "id" in comp:
        if self.id != comp["id"]:
            return False
    if "order_id" in comp:
        if self.order_id != comp["order_id"]:
            return False
    return True