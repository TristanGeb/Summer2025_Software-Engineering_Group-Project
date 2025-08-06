from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(256),nullable = False)
    
    pay_name = Column("pay_name",String(256),nullable = False)#Name on card
    pay_num = Column(String(256),nullable = False) #Card number
    pay_sec = Column(String(256),nullable = False) #CVV
    
    email = Column(String(256),unique = True, nullable = False)
    phone_num = Column(String(256),unique = True, nullable = False)     
    address = Column(String(256),nullable = False)
    
    username = Column(String(256),nullable = False)
    password = Column(String(256),nullable = False)

    def __repr__(self):
        return f"({self.id},{self.name})"


#FOR testing purposes
def compare(self, comp):
    if "id" in comp:
        if self.id != comp["id"]:
            return False
    if "name" in comp:
        if self.name != comp["name"]:
            return False
    if "pay_name" in comp:
        if self.pay_name != comp["pay_name"]:
            return False
    if "pay_num" in comp:
        if self.pay_num != comp["pay_num"]:
            return False
    if "pay_sec" in comp:
        if self.pay_sec != comp["pay_sec"]:
            return False
    if "email" in comp:
        if self.email != comp["email"]:
            return False
    if "phone_num" in comp:
        if self.phone_num != comp["phone_num"]:
            return False
    if "address" in comp:
        if self.address != comp["address"]:
            return False
    if "username" in comp:
        if self.username != comp["username"]:
            return False
    if "password" in comp:
        if self.password != comp["password"]:
            return False
    return True