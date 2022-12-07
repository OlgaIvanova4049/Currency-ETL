import bcrypt
from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from orm.models.user import UserModel
from orm.schemas.user import UserLoginSchema


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)


def get_user_by_username(username: str, db):
    query = select(UserModel).filter(UserModel.username == username)
    result = db.execute(query)
    return result.scalars().first()


def create_user(data, db):
    user = get_user_by_username(data.username, db)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"user with name {data.username} already exists",
        )
    else:
        hashed_password = get_hashed_password(data.password)
        user = UserModel(username=data.username, password=hashed_password)
        db.add(user)
        db.commit()


def check_user(data: UserLoginSchema, db):
    query = select(UserModel).filter(UserModel.username == data.username)
    result = db.execute(query)
    user = result.scalars().first()
    return check_password(data.password, user.password)
