from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Acounts(Base):
    __tablename__ = "sandwiches"

    account_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    pay_name = Column(String(256),nullable = False) 
    pay_num = Column(String(256),nullable = False) #Name on card
    pay_sec = Column(String(256),nullable = False) #Card#

    email = Column(String(256),unique = True, nullable = False) #CVV
    phone_num = Column(String(256),unique = True, nullable = False)     
    address = Column(String(256),nullable = False)
