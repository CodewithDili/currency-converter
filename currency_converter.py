import requests

# Replace with your ExchangeRate-API key
API_KEY = ' c8d0a6a4f92e01c9e0e67769'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

def get_exchange_rate(from_currency, to_currency):
    """
    Fetches the exchange rate from one currency to another using the ExchangeRate-API.
    
    Parameters:
        from_currency (str): The currency code to convert from (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'EUR').
    
    Returns:
        float: The exchange rate from the source currency to the target currency.
    """
    url = f"{BASE_URL}/{API_KEY}/latest/{from_currency}"
    print(f"Requesting URL: {url}")  # Debug print
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")  # Debug print
    print(f"Response text: {response.text}")  # Debug print
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching exchange rate: {data.get('error-type', 'Unknown error')}")
    
    if to_currency not in data['conversion_rates']:
        raise Exception(f"Currency {to_currency} not found in conversion rates.")
    
    return data['conversion_rates'][to_currency]

def convert_currency(amount, from_currency, to_currency):
    """
    Converts a given amount from one currency to another using the fetched exchange rate.
    
    Parameters:
        amount (float): The amount to convert.
        from_currency (str): The currency code of the amount (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'EUR').
    
    Returns:
        float: The converted amount in the target currency.
    """
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

if __name__ == "__main__":
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        print(f"Error: {e}")
