from fastapi import FastAPI
from pydantic import BaseModel
from app.api import users, auth, offers, transactions
app = FastAPI()
class Listing(BaseModel):
    title: str
    type: str
    price: float | None = None
@app.get("/")
def root():
    return {"message": "Barter backend is live"}
@app.get("/listings")
def get_listings():
    return [
        {"id": 1, "title": "Guitar Lessons", "type": "service"},
        {"id": 2, "title": "Old Laptop", "type": "item"}
    ]
@app.post("/listings")
def create_listing(listing: Listing):
    return listing
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(offers.router, prefix="/offers", tags=["Offers"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])