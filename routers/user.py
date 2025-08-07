from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter(prefix="/user", tags=["User Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put("/{user_id}")
def edit_user(user_id: int, updates: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, updates)