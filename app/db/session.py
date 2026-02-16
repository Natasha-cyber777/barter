import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

# Import models so tables get created
from app.models.transaction import Transaction
from app.models.user import User
from app.models.listing import Listing
from app.models.message import Message
from app.models.offer import Offer
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Local fallback if not on Railway
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/bartr"

# ✅ Fix Railway old postgres:// format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
