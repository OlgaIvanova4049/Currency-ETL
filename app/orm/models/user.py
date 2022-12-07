from sqlalchemy import Column, String, Integer

from orm.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(
        Integer(),
        primary_key=True,
    )
    username = Column(String(120), unique=True)
    password = Column(String())
