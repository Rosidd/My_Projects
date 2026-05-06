from fastapi import HTTPException
from models import fetch_all_currencies, fetch_rate
from schemas import CurrencyResponse, ExchangeRate

allowed_currencies = ["USD", "EUR", "INR", "AED", "AUD", "CAD,"]

def get_currency_master():
    rows = fetch_all_currencies()

    response = {}
    for r in rows:
        response[r['currency_code']] = {
            "country_name": r['country_name'],
            "currency_name": r['currency_name'],
            "currency_code": r['currency_code']
        }
    return response

def validate_currency_code(currency_code: str):
    if currency_code not in allowed_currencies:
        raise HTTPException(status_code=400, detail=f"Invalid currency code: {currency_code}")
    
def calculate_exchange_rate(currency_code_from: str, currency_code_to: str):
    validate_currency_code(currency_code_from)
    validate_currency_code(currency_code_to)

    if currency_code_from == currency_code_to:
        return 1.0

    direct_rate = fetch_rate(currency_code_from, currency_code_to)
    if direct_rate:
        return direct_rate
    
    inverse_rate = fetch_rate(currency_code_to, currency_code_from)
    if inverse_rate:
        return (1 / inverse_rate,6)
    raise HTTPException(status_code=404, detail=f"Exchange rate not found for {currency_code_from} to {currency_code_to}")