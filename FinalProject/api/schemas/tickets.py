from pydantic import BaseModel
from typing import Optional


class TicketBase(BaseModel):
    body: str
    account: int
class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    body: Optional[str] = None
    account: Optional[int] = None

class Ticket(TicketBase):
    id: int
    
    class Config:
        from_attributes = True