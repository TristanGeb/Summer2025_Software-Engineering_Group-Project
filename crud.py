from sqlalchemy.orm import Session
from models import GuestOrder, User, PromoCode
from schemas import GuestOrderCreate, UserUpdate, PromoCreate
from datetime import date
import uuid

def create_guest_order(db: Session, order: GuestOrderCreate):
    tracking_number = f"GUEST-{uuid.uuid4().hex[:8]}"
    db_order = GuestOrder(**order.dict(), tracking_number=tracking_number)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_user(db: Session, user_id: int, update: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    return user

def create_promo(db: Session, promo: PromoCreate):
    db_promo = PromoCode(**promo.dict())
    db.add(db_promo)
    db.commit()
    db.refresh(db_promo)
    return db_promo

def get_all_promos(db: Session):
    return db.query(PromoCode).filter(PromoCode.is_active == True).all()

def apply_promo_code(db: Session, code: str, total: float):
    promo = db.query(PromoCode).filter(PromoCode.code == code, PromoCode.is_active == True).first()
    if not promo or promo.expiry_date < date.today():
        return None
    discount_amount = (promo.discount / 100) * total
    return round(total - discount_amount, 2), round(discount_amount, 2)