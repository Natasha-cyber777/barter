from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    sender_id = Column(Integer)
    
    offered_mode = Column(String)   # barter / cash / mixed
    offered_price = Column(Integer, nullable=True)
    message = Column(String)

    status = Column(String, default="pending")
