
from decimal import Decimal
from pydantic import BaseModel

class KCModel(BaseModel):
    id: int
    price: Decimal
    bedrooms: int
    bathrooms: Decimal
    sqft_living: int

    class Config:
        orm_mode = True
        
class KCOut(BaseModel):
    id: int
    price: Decimal
    bedrooms: int
    bathrooms: Decimal
    sqft_living: int
    
    class Config:
        orm_mode = True

class KCUpdate(BaseModel):
    price: Decimal
    bedrooms: int
    bathrooms: Decimal
    sqft_living: int
    
    class Config:
        orm_mode = True