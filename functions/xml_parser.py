import bs4

from functions.currency_schema import CurrencySchema

currencies = ["USD", "EUR"]


def parse_xml_data(response):
    soup = bs4.BeautifulSoup(response.content, features="xml")
    currency_rates = []
    for v in soup.find_all(name="Valute"):
        currency = str(v.find(name="CharCode").text)
        if currency in currencies:
            currency_rates.append(
                {
                    "code": currency,
                    "nominal": v.find(name="Nominal").text,
                    "value": v.find(name="Value").text.replace(",", "."),
                }
            )
    return [CurrencySchema(**currency) for currency in currency_rates]
