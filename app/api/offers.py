from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models.offer import Offer

router = APIRouter(prefix="/offers", tags=["Offers"])

@router.post("/")
def create_offer(
    listing_id: int,
    message: str,
    db: Session = Depends(get_db)
):
    offer = Offer(
        listing_id=listing_id,
        sender_id=1,  # temp
        offered_mode="barter",
        message=message
    )
    db.add(offer)
    db.commit()
    return offer
