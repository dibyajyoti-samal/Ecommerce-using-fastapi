from sqlmodel import SQLModel,create_engine,Session
from typing import Annotated
from fastapi import Depends
db_name="Users.db"
db_url=f"sqlite:///{db_name}"
connect_args={"check_same_thread":False}

engine=create_engine(db_url,connect_args=connect_args)

async def creat_db_and_table():
    SQLModel.metadata.create_all(engine)

async def get_db_session():
    with Session (engine) as session:
        yield session

SessionDep=Annotated[Session,Depends(get_db_session)]

