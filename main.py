from fastapi import FastAPI
from routers import guest, user, promo
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(guest.router)
app.include_router(user.router)
app.include_router(promo.router)