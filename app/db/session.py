from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
# CRITICAL: You must import your models so Base 'registers' them
from app.models.users import User 

DATABASE_URL = "postgresql://postgres:rPNdAhQFnFZVHsZTmhQqPvmoWIzgOpox@postgres.railway.internal:5432/railway"

engine = create_engine(DATABASE_URL)

# This command now 'sees' the User class and creates the "users" table
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)