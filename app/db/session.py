import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
# Importing all models ensures they are all created in the DB at once
from app.models.user import User 
from app.models.listing import Listing
from app.models.message import Message

# This looks for the 'DATABASE_URL' variable you saw in the Railway dashboard
DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback for local development (optional)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

# Syncs your Python models with the PostgreSQL tables
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()