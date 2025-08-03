import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routers import index as indexRoute
from api.models import model_loader
from api.dependencies.config import conf
from api import models
from api import controllers
from api.dependencies.tempdatabase import SessionLocal
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)

test_data1 = {
    "name": "John Doe",
    "pay_name": "John D",
    "pay_num": "1346321343",
    "pay_sec": "235",
    "email": "JD@gmail.com",
    "phone_num": "123 424 1234",
    "address": "123 address drive",
    "username": "JohnUserName",
    "password": "JohnPassword"
}

session = SessionLocal()
#account1= models.Accounts(test_data1)
test_object1 = models.accounts.Accounts(**test_data1)
created_test_object1 = controllers.accounts.create(session, test_object1)
print(created_test_object1)