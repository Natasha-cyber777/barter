from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.listing import ListingCreate
from app.models.listing import Listing
from app.deps import get_db

router = APIRouter(prefix="/listings", tags=["Listings"])

@router.post("/")
def create_listing(
    listing: ListingCreate,
    db: Session = Depends(get_db)
):
    db_listing = Listing(**listing.dict(), owner_id=1)  # temp user
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing
@router.get("/")
def get_listings(db: Session = Depends(get_db)):
    return db.query(Listing).all()
