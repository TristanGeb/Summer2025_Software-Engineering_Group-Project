from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..dependencies.database import Base

class Tickets(Base):
    __tablename__ = "tickets"
   
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    body = Column(String(256),nullable = False)
    account = Column(Integer, ForeignKey("accounts.id"))


def compare(self, comp):
    if "id" in comp:
        if self.id != comp["id"]:
            return False
    if "body" in comp:
        if self.body != comp["body"]:
            return False
    if "account" in comp:
        if self.account != comp["account"]:
            return False
    return True