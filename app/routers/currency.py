import datetime
import http

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from auth.auth_bearer import JWTBearer
from orm.database import get_db
from services.currency_services import (
    add_currency_for_date,
    get_currency_rate_for_date,
)

router = APIRouter()


@router.post(
    "/",
    status_code=http.HTTPStatus.CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["currency"],
)
def currency_for_date(date: datetime.date = Body(..., embed=True)):
    return add_currency_for_date(date)


@router.get("/", dependencies=[Depends(JWTBearer())], tags=["currency"])
def currency_for_date(date: datetime.date, db: Session = Depends(get_db)):
    return get_currency_rate_for_date(date, db)
