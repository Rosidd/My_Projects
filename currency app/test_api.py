from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_currencies():
    response = client.get("/currency")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "USD" in data
    assert "EUR" in data

def test_exchange_rate_direct_or_inverse():
    response = client.get("/exchange-rate/USD/EUR")
    assert response.status_code == 200
    data = response.json()
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "EUR"
    assert isinstance(data["exchange_rate"], (int, float))

def test_invalid_currency():
    response = client.get("/exchange-rate/XYZ/USD")
    assert response.status_code == 400
    data = response.json()
    assert "Invalid currency code" in data["detail"]