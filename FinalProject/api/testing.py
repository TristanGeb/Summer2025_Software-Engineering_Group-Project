import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routers import index as indexRoute
from api.models import model_loader
from api.dependencies.config import conf
import api.printinfo as he
import logging
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
indexRoute.load_routes_admin(app)

#log=logging.getLogger(__name__)
#uvicorn.run(app, host=conf.app_host, port=conf.app_port)
import api.testingresources
def test_1():
    print("here")
    #log.critical("aa")
    #response = app.get("/accounts")
    #print(response.json())
    #he.showinfo(response)
    #assert response.status_code ==
    assert 1==2
