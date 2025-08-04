from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Orders(Base):
    __tablename__ = "all_orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    date = Column(Date, nullable=False, default=date.today)
    total = Column(DECIMAL(10, 2), nullable=False)