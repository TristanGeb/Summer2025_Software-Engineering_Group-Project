from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..dependencies.database import engine, get_db
from ..schemas.orders_current import OrderStatus, UpdateStatus, OrderStatusResponse
from ..controllers import orders as controller

router = APIRouter(
    prefix = "/staff/orders",
    tags=["Staff Orders"]
)

#Get active orders for kitchen staff
@router.get("/", response_model = list[OrderStatusResponse])
def get_active_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

#Get one order's status
@router.get("/{order_id}", response_model = OrderStatusResponse)
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    return controller.get_status(db, order_id)

#Update the status, such as preparing, ready, completed
@router.put("/{order_id}/status", response_model = OrderStatusResponse)
def update_order_status(order_id: int, request: UpdateStatus, db: Session = Depends(get_db)):
    return controller.update_status(db, order_id, request.status)

#Manager route to view full history of orders
@router.get("/all", response_model = list[OrderStatusResponse])
def get_all_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)