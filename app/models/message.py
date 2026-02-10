from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    sender_id = Column(Integer)
    content = Column(String)
