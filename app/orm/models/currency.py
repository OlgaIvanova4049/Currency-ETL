from sqlalchemy import Column, String, Date, Integer, Float

from orm.models.base import Base


class CurrencyModel(Base):
    __tablename__ = "currencies"

    code = Column(String(5), primary_key=True)
    date = Column(Date, primary_key=True)
    nominal = Column(Integer())
    value = Column(Float())
