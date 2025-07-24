from pydantic import BaseModel
from typing import Optional


class AccountBase(BaseModel):
    name: str
    pay_name : str
    pay_num : str
    pay_sec : str
    
    email : str
    phone_num : str
    address : str
    
    username : str
    password : str
    
class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    pay_name: Optional[str] = None
    pay_num: Optional[str] = None
    pay_sec: Optional[str] = None
    email: Optional[str] = None
    phone_num: Optional[str] = None
    address: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

class Account(AccountBase):
    account_id: int
    
    class Config:
        from_attributes = True