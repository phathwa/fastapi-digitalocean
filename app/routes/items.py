from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.schemas import ItemCreate, ItemResponse
from app.database import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_item(db=db, item=item)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Item with this ID already exists")

@router.get("/items/", response_model=list[ItemResponse])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
