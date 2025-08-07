from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/promo", tags=["Promo Codes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PromoOut)
def create_promo(promo: schemas.PromoCreate, db: Session = Depends(get_db)):
    return crud.create_promo(db, promo)

@router.get("/", response_model=list[schemas.PromoOut])
def view_promos(db: Session = Depends(get_db)):
    return crud.get_all_promos(db)

@router.post("/apply")
def apply_promo(promo: schemas.PromoApply, db: Session = Depends(get_db)):
    result = crud.apply_promo_code(db, promo.promo_code, promo.order_total)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid or expired promo code")
    return {"discounted_total": result[0], "discount_amount": result[1]}