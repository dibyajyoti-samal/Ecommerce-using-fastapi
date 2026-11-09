from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import creat_db_and_table
from app.routers import Users

@asynccontextmanager
async def lifespan(app:lifespan):
    print("Start")
    await creat_db_and_table()
    yield
    print("Stop")

app = FastAPI(lifespan=lifespan)

app.include_router(Users.router,prefix="/User",tags=["UsersAPI"])

    

