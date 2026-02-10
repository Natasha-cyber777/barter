from pydantic import BaseModel
from typing import Optional

class ListingCreate(BaseModel):
    title: str
    description: str
    category: str
    listing_type: str
    value_mode: str
    price: Optional[float] = None
