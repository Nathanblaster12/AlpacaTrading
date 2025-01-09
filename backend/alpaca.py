from alpaca_trade_api.rest import REST as TradingClient
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from environment variables
alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

trading_client = TradingClient(
    key_id=alpaca_api_key,
    secret_key=alpaca_secret_key,
    base_url='https://paper-api.alpaca.markets'
)

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)

