from sqlmodel import SQLModel, Field


class User(SQLModel):
    first_name: str
    last_name: str
    email: str
 
    

class UserRegister(User,table=True):
    id: int | None = Field(default=None, primary_key=True)
    password:str
    conpassword:str



   