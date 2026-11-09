from fastapi import APIRouter,Depends
from app.models import UserInput
from app.database import get_db_session,SessionDep


router = APIRouter()


@router.post("/register")
async def get_user(user_regi_detail:UserInput,session:SessionDep):
    reg_user_data=UserInput(**user_regi_detail.model_dump())
    session.add(reg_user_data)
    session.commit()
    session.refresh(reg_user_data)
    return reg_user_data

