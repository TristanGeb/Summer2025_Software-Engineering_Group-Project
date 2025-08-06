from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promos as controller
from ..schemas import promos as schema
from ..schemas.promos import Promos as Schema
from ..schemas.promos import PromosBase as SchemaBase
from ..schemas.promos import PromosCreate as SchemaCreate
from ..schemas.promos import PromosUpdate as SchemaUpdate


from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promos'],
    prefix="/promos"
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
