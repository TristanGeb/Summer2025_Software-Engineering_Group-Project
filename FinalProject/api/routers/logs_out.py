from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import logs_out as controller
from ..schemas import logs_out as schema
from ..schemas.logs_out import Logout as Schema
from ..schemas.logs_out import LogoutBase as SchemaBase
from ..schemas.logs_out import LogoutLogCreate as SchemaCreate



from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Logout'],
    prefix="/logs_out"
)

#logs logout attempts in logout_logs table
@router.post("/", response_model=Schema,status_code=status.HTTP_201_CREATED)
def logout(request: SchemaCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

#read all logs/attempts
@router.get("/", response_model=list[Schema])
def read_all_attempts(db: Session = Depends(get_db)):
    return controller.read_all(db)

