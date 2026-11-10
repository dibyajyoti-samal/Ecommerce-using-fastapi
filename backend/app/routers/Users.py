from fastapi import APIRouter,Depends
from app.models import User,UserRegister
from app.database import SessionDep

router = APIRouter()

@router.post("/register")
async def get_user(user_regi_detail:User,session:SessionDep):
    new_user = UserRegister(**user_regi_detail.model_dump())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.get("/getUser/{user_id}")
async def get_user_detail(user_id:int,session:SessionDep):
    get_user_data=session.get(User,user_id)
    return get_user_data
