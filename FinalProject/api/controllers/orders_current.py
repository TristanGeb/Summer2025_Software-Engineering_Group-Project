from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import orders_current as model
from ..models.orders_current import CurrentOrders as Models


def create(db: Session, request):
    new_item = Models(
        order_id=request.order_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_item

def delete(db: Session, item_id):
    try:
        item = db.query(Models).filter(Models.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def read_all(db: Session):
    try:
        result = db.query(Models).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(Models).filter(Models.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(Models).filter(Models.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(Models).filter(Models.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Controller logic for order status
def update_status(db: Session, order_id: int, new_status: str):
    order = db.query(model.CurrentOrders).filter(model.CurrentOrders.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    order.status = new_status
    db.commit()
    db.refresh(order)
    return {"order_id": order_id, "status": order.status}


def get_status(db: Session, order_id: int):
    order = db.query(model.CurrentOrders).filter(model.CurrentOrders.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    return {"order_id": order_id, "status": order.status}


# Controller logic to see active/pending orders, meant for kitchen staff
def read_all_active(db: Session):
    return db.query(model.CurrentOrders).filter(model.CurrentOrders.status.in_([model.CurrentOrders.pending,
                                                                                model.OrderStatus.preparing,
                                                                                model.OrderStatus.ready])).all()