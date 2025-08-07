from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/guest", tags=["Guest Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order", response_model=schemas.GuestOrderOut)
def place_guest_order(order: schemas.GuestOrderCreate, db: Session = Depends(get_db)):
    return crud.create_guest_order(db, order)