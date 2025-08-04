from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    amount_in_storage=Column(Integer, nullable=False)


    def __repr__(self):
        return f"(id={self.id},  name={self.name},   amount_in_storage={self.amount_in_storage}"