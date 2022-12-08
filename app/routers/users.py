from fastapi import APIRouter, Body, Depends

from auth.handler import sign_jwt
from orm.database import get_db
from orm.schemas.user import UserSchema
from services.user_services import create_user, check_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/signup")
def signup_user(user: UserSchema = Body(...), db=Depends(get_db)):
    create_user(user, db)
    return sign_jwt(user.username)


@router.post("/login")
async def user_login(user: UserSchema = Body(...), db=Depends(get_db)):
    if check_user(user, db):
        return sign_jwt(user.username)
    return {"error": "Wrong login details!"}
