# run.py
from data.db import init_db, SessionLocal
from utils.iss_moex_client.py import get_market_data

def main():
    init_db()
    session = SessionLocal()

    symbol = "GAZP"
    market_data = get_market_data(symbol)
    if market_data:
        print(market_data)
    else:
        print("Error fetching market data")

if __name__ == "__main__":
    main()
