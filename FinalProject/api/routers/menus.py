from http.client import responses

from fastapi import APIRouter, Depends, FastAPI, status, Response
from fastapi.openapi.models import Schema
from sqlalchemy.orm import Session
from ..controllers import menus as controller
from ..schemas import menus as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags = ['Menus'],
    prefix = "/menus"
)

@router.post("/", response_model = schema.Menu)
def create(request: Schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db = db, request = request)

@router.get("/", response_model = list[schema.Menu])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_id}", response_model = schema.Menu)
def read_one(menu_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_id = menu_id)

@router.put("/{menu_id}", reponse_model = schema.Menu)
def update(menu_id: int, request: schema.Menu, db: Session = Depends(get_db)):
    return controller.update(db=db, request = request, menu_id = menu_id)

@router.delete("/{menu_id}")
def delete(menu_id: int, db: Session = Depends(get_db)):
    return controller.delete(db = db, menu_id = menu_id)
