from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menus, menu_items

#create new instance of a menu
def create(db: Session, menu):
    new_item = menus.Menu(
        menu_id = menus.menu_id,
        menu_name = menus.menu_name
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = error)
    return new_item

def read_all(db: Session):
    try:
        result = db.query(menus.Menu).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = error)
    return result

def read_one(db: Session, menu_id):
    try:
        menu = db.query(menus.Menu).filter(menus.Menu.id == menu_id).first()
        if not menu:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Menu ID not found")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = error)
    return menu

def update(db: Session, menu_id, request):
    try:
        menu = db.query(menus.Menu).filter(menus.Menu.id == menu_id)
        if not menu.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Menu ID not found")
        update_data = request.dict(excluse_unset=True)
        menu.update(update_data, synchronize_session = False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return menu.first()

def delete(db: Session, menu_id):
    try:
        menu = db.query(menus.Menu).filter(menus.Menu.id == menu_id)
        if not menu.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Menu ID not found")
        menu.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)