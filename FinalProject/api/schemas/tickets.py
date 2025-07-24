from pydantic import BaseModel
from typing import Optional


class TicketBase(BaseModel):
    pass
    
class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    pass

class Ticket(TicketBase):
    tix_id: int
    
    class Config:
        from_attributes = True