from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class OrderHistory(Base):
    __tablename__ = "orders_all"
    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    date = Column(Date, nullable=False, default=date.today)
    total = Column(DECIMAL(10, 2), nullable=False)

    orders_current = relationship("CurrentOrders", back_poplates = "order_history")