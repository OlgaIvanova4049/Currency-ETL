import requests
from fastapi import Depends
from sqlalchemy import select

from core.settings import settings
from orm.models.currency import CurrencyModel
from orm.schemas.currency import Currency


def add_currency_for_date(date) -> dict:
    requests.post(
        url=settings.FUNCTION_URL,
        data={"date": date},
        headers={"Content-Type": "application/json"},
    )
    return {"message": "Record created"}


def get_currency_rate_for_date(date, db=Depends()) -> list[Currency]:
    query = select(CurrencyModel).filter(CurrencyModel.date == date)
    result = db.execute(query)
    currencies = result.scalars().all()
    return [Currency.from_orm(currency) for currency in currencies]
