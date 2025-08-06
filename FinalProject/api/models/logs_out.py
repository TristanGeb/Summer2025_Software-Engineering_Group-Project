from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Logout(Base):
    __tablename__ = "logout_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    timestamp = Column(DateTime, default=datetime.UTC)
    
    username = Column(String(256),nullable = False)
    password = Column(String(256),nullable = False)
    
    success = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"({self.id},{self.username})"
