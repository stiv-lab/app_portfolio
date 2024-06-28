# utils/iss_moex_client.py
import requests

BASE_URL = "https://iss.moex.com/iss"

def get_market_data(symbol):
    endpoint = f"{BASE_URL}/engines/stock/markets/shares/boards/TQBR/securities/{symbol}.json"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return None
