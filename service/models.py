
from sqlalchemy import Boolean, Float, Column, ForeignKey, Integer, String
from database import Base

class KCdata(Base):
    __tablename__ = "public.kingcountydata"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Float)
    sqft_living = Column(Integer)