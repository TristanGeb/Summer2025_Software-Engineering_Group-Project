from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import logs_out as model
from ..models.logs_out import Logout as Models
from ..models.accounts import Accounts as AccountModel


def create(db: Session, request):
    
# checking BOTH entered usernames/passwords are right
    account = db.query(AccountModel).filter(
        AccountModel.username == request.username,
        AccountModel.password == request.password,
    ).first()
    
    if not account:
        raise HTTPException(status_code=401, detail="User is not logged in.")
    elif account:
        success = True
        account_id = account.id
    else:
        success = False
        account_id = None
    
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = "Invalid Credentials")
    
    
    new_item = Models(
        username = request.username,
        password = request.password,
        account_id = account_id,
        success = success
    )

    try:
       
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error)
   
    return new_item




def read_all(db: Session):
    try:
        result = db.query(Models).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error)
    return result






