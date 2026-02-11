from fastapi import FastAPI
from pydantic import BaseModel
from app.api import listings, users, auth, offers, transactions
from fastapi.middleware.cors import CORSMiddleware
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
app.include_router(listings.router)
app.include_router(offers.router)
app.include_router(transactions.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/health")
def health():
    return {"status": "ok"}
