from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.offer import Offer
from app.deps import get_db

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/accept/{offer_id}")
def accept_offer(offer_id: int, db: Session = Depends(get_db)):
    offer = db.query(Offer).get(offer_id)
    offer.status = "accepted"

    tx = Transaction(
        listing_id=offer.listing_id,
        initiator_id=offer.sender_id,
        receiver_id=1,
        mode=offer.offered_mode
    )

    db.add(tx)
    db.commit()
    return tx
