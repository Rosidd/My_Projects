from fastapi import FastAPI
from pydantic import BaseModel 
from services import get_currency_master, calculate_exchange_rate
from schemas import CurrencyResponse, ExchangeRate

app = FastAPI(title="Currency Exchange RateAPI", version="1.0")

@app.get("/currency", response_model=dict[str, CurrencyResponse])

def get_currency():
    """ GET /currency 
    Returns a map of currency codes to their details (country name, currency name, and currency code) for all active currencies in the database."""
    return get_currency_master()

@app.get("/exchange-rate/{currency_code_from}/{currency_code_to}", response_model=ExchangeRate)

def get_exchange_rate(currency_code_from: str, currency_code_to: str):
    """ GET /exchange-rate/{currency_code_from}/{currency_code_to} 

    Returns the exchange rate from the specified source currency to the target currency. If the exchange rate is not found, it returns a 404 error."""

    exchange_rate = calculate_exchange_rate(currency_code_from, currency_code_to)
    
    return ExchangeRate(
        from_currency=currency_code_from,
        to_currency=currency_code_to,
        exchange_rate=exchange_rate
    )