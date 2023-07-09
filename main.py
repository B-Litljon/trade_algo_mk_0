# imports
import sys
import asyncio
from helpers.binance_ws_connect import binance_websocket 
from helpers.binance_api import binanceus_request


# when running this script you must do so like: 
# `python main.py argv[1] argv[2]`
# currently this implementation will only allow a user to monitor price of one currency at a time
# #
if __name__ == '__main__':
    base_currency = sys.argv[1]
    quote_currency = sys.argv[2]
    # data collection/analysis 
    asyncio.run(binance_websocket(base_currency, quote_currency))


# algo logic 

# execute orders 
