import datetime

import requests
import psycopg2

from functions.xml_parser import parse_xml_data

connection = psycopg2.connect(
    database="currency",  # Идентификатор подключения "akfiotqh2m**********"
    user="user",  # Пользователь БД
    password="password",
    host="localhost",  # Точка входа "akfiotqh2m**********.postgresql-proxy.serverless.yandexcloud.net"
    port=5434,
)


def get_daily_currency(date: datetime.date):
    date_request = date.strftime("%d/%m/%Y")
    response = requests.get(
        f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_request}"
    )
    return parse_xml_data(response)


def handler(event, context):
    if body := event.get("body", {}):
        date = body.get("date")
        date = datetime.date.fromisoformat(date)
    else:
        date = datetime.date.today()
    currency_rates = get_daily_currency(date)
    cursor = connection.cursor()
    for rate in currency_rates:
        rate.date = date
        query = """SELECT * FROM currencies WHERE date = %(date)s AND code = %(code)s"""
        cursor.execute(query, rate.dict())
        result = cursor.fetchone()
        if not result:
            cursor.execute(
                f"""INSERT INTO currencies
                                VALUES (%(code)s, %(date)s, %(nominal)s, %(value)s)
            """,
                rate.dict(),
            )
        connection.commit()
    return {"status": 200, "data": currency_rates}


# print(handler({"body": {"date": "2022-11-18"}}, "context"))
print(handler({"body": None}, "context"))
