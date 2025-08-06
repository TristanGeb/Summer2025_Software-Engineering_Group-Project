from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import logs_in as controller
from ..schemas import logs_in as schema
from ..schemas.logs_in import Login as Schema
from ..schemas.logs_in import LoginBase as SchemaBase
from ..schemas.logs_in import LoginLogCreate as SchemaCreate



from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Login'],
    prefix="/logs_in"
)

#logs login attempts in login_logs table
@router.post("/", response_model=Schema,status_code=status.HTTP_201_CREATED)
def login(request: SchemaCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

#read all logs/attempts
@router.get("/", response_model=list[Schema])
def read_all_attempts(db: Session = Depends(get_db)):
    return controller.read_all(db)

#read all SUCCESSFUL logs 
@router.get("/success", response_model=list[Schema])
def read_succesful(db: Session = Depends(get_db)):
    return controller.read_succesful(db)

#read all FAILED logs 
@router.get("/failed", response_model=list[Schema])
def read_failed(db: Session = Depends(get_db)):
    return controller.read_failed(db)
