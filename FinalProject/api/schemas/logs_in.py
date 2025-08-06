from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoginBase(BaseModel):
    username: str
    password : str
    
    
class LoginLogCreate(LoginBase):
    pass



class Login(LoginBase):
    id: int
    account_id: Optional[int] = None
    success:bool
    timestamp:datetime
    
    class Config:
        from_attributes = True