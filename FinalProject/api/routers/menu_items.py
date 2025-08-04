from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..schemas.menu_items import MenuItem as Schema
from ..schemas.menu_items import MenuItemBase as SchemaBase
from ..schemas.menu_items import MenuItemCreate as SchemaCreate
from ..schemas.menu_items import MenuItemUpdate as SchemaUpdate


from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu_items'],
    prefix="/menu_items"
)


@router.post("/", response_model=Schema)
def create(request: SchemaCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[Schema])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=Schema)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=Schema)
def update(item_id: int, request: SchemaUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
