print("MAIN APP LOADED")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import listings, users, auth, offers, transactions

app = FastAPI(
    
    title="Barter Backend",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------
# BASIC SYSTEM ROUTES
# -----------------------

@app.get("/")
def root():
    return {"message": "Barter backend is live"}

@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------
# API ROUTERS
# -----------------------

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(listings.router)
app.include_router(offers.router)
app.include_router(transactions.router)

# -----------------------
# CORS CONFIG
# -----------------------

