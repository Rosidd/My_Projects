from pydantic import BaseModel

class CurrencyResponse(BaseModel):
    country_name: str
    currency_name: str
    currency_code: str

class ExchangeRate(BaseModel):
    from_currency: str
    to_currency: str
    exchange_rate: float