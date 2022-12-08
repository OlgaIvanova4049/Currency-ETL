import bcrypt
from sqlalchemy import select

from exceptions.bad_request import BadRequestException
from orm.models.user import UserModel
from orm.schemas.user import UserSchema


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
        raise BadRequestException(detail=f"user with name {data.username} already exists")
    else:
        hashed_password = get_hashed_password(data.password)
        user = UserModel(username=data.username, password=hashed_password)
        db.add(user)
        db.commit()


def check_user(data: UserSchema, db):
    user = get_user_by_username(data.username, db)
    return check_password(data.password, user.password)
