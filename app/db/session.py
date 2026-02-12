from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
# This import tells SQLAlchemy to include the User model in the metadata
from app.models.user import User 

# It is better to use an environment variable, but I am using your 
# string directly here to ensure it works immediately on Railway.
DATABASE_URL = "postgresql://postgres:rPNdAhQFnFZVHsZTmhQqPvmoWIzgOpox@postgres.railway.internal:5432/railway"

engine = create_engine(DATABASE_URL)

# This is the "Magic Link" that creates your tables in the database
# It looks at 'User' imported above and creates the 'users' table if it doesn't exist.
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()