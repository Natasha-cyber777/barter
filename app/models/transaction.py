from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    initiator_id = Column(Integer)
    receiver_id = Column(Integer)

    mode = Column(String)   # barter / cash / mixed
    status = Column(String, default="pending")
