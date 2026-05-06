from db import get_db_connection

def fetch_all_currencies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT country_name, currency_name, currency_code FROM currency")
    currency = cursor.fetchall()
    cursor.close()
    connection.close()
    return currency

def fetch_rate(currency_code_from, currency_code_to):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT exchange_rate FROM currency_rate
    WHERE currency_code_from = %s AND currency_code_to = %s;
    """
    cursor.execute(query, (currency_code_from, currency_code_to))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if result:
        return result['exchange_rate']
    else:
        raise ValueError(f"Exchange rate not found for {currency_code_from} to {currency_code_to}")