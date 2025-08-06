from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models import logs_in as model
from ..models.logs_in import Login as Models
from ..models.accounts import Accounts as AccountsModel


def create(db: Session, request):
    
#TODO if statement checking if BOTH entered usernames and passwords are right
    user = db.query(AccountsModel).filter(
        AccountsModel.username == request.username,
        AccountsModel.password == request.password
    ).first()
    
    if user:
        success = True
        account_id = user.id
    else:
        success = False
        account_id = None
        
        failed_log = model.Login(
            username=request.username,
            password=request.password,
            success=False,
            account_id=None  # if no matching account, set to None or 0
        )
        
        #add failed attempt logs
        db.add(failed_log)
        db.commit()
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
        raise HTTPException(status_code=status.HTTP_401_BAD_REQUEST, detail=error)
   
    return new_item




def read_all(db: Session):
    try:
        result = db.query(Models).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_401_BAD_REQUEST, detail=error)
    return result

def read_succesful(db: Session):
    return db.query(model.Login).filter(model.Login.success == True).all()

def read_failed(db: Session):
    return db.query(model.Login).filter(model.Login.success == False).all()




