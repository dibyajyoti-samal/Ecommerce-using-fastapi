from pydantic import BaseModel,EmailStr


class UserInput(BaseModel):
    firstname:str
    lastname:str
    email:str
    age:int
    gender:str

