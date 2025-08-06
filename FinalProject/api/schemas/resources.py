from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    name: str
    amount_in_storage: int

class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    name: Optional[str] = None
    amount_in_storage: int

class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
