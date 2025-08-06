from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogoutBase(BaseModel):
    username: str
    password : str
    
    
class LogoutLogCreate(LogoutBase):
    pass



class Logout(LogoutBase):
    id: int
    account_id: Optional[int] = None
    success:bool
    timestamp:datetime
    
    class Config:
        from_attributes = True