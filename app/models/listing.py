from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    
    listing_type = Column(String)  # item / service
    value_mode = Column(String)    # barter / cash / both
    price = Column(Float, nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
