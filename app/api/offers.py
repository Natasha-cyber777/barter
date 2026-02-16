from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db, get_current_user
from app.models.offer import Offer
from app.models.user import User
from app.models.listing import Listing

router = APIRouter(prefix="/offers", tags=["Offers"])


@router.post("/")
def create_offer(
    listing_id: int,
    message: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print("AUTH USER ID:", current_user.id)
    # Optional but recommended: verify listing exists
    listing = db.query(Listing).filter(Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    offer = Offer(
        listing_id=listing_id,
        sender_id=current_user.id,   # 🔥 real authenticated user
        offered_mode="barter",
        message=message,
        status="pending"
    )

    db.add(offer)
    db.commit()
    db.refresh(offer)

    return offer
