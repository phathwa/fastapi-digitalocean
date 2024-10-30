from fastapi import FastAPI
from app.routes import items
from app.database import engine
from app.models import Base

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
api = FastAPI()

# Include the items router
api.include_router(items.router)

@api.get("/")
async def home():
    return {"message": "Hello World"}
