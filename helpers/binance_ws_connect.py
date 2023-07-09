import asyncio
import json
import websockets
import pandas as pd
import sys

async def binance_websocket(base_currency, quote_currency):
    pair = base_currency.lower() + quote_currency.lower()
    uri = f"wss://stream.binance.us:9443/ws/{pair}@kline_1s"
    price_df = pd.DataFrame(columns=["Timestamp", "Open", "High", "Low", "Close"]) 
    async with websockets.connect(uri) as websocket:
        async for message in websocket:

            # rows for dataframe
            data = json.loads(message)
            timestamp = pd.Timestamp.now()
            open_price = float(data["k"]["o"])
            high_price = float(data["k"]["h"])
            low_price = float(data["k"]["l"])
            close_price = float(data["k"]["c"])
            
            websocket_data = pd.DataFrame({
                "Timestamp": [timestamp],
                "Open": [open_price],
                "High": [high_price],
                "Low": [low_price],
                "Close": [close_price]
            })
            
            price_df = pd.concat([price_df, websocket_data], ignore_index=True)
                         
            print(price_df.head())

# NOTE FOR FUTURE SELF:
# so we got the websocket connection working and are storing the data into a pandas df!
# however we need to create a more dynamic df that will only print out the data one time, 
# then replace the values upon changes in the data. that way we're not getting a constant stream of data thats difficult to decipher
# #


# json response example from binance websocket api 'klines'
# {
#   "e": "kline",     // Event type
#   "E": 1672515782136,   // Event time
#   "s": "BNBBTC",    // Symbol
#   "k": {
#     "t": 1672515780000, // Kline start time  ~
#     "T": 1672515839999, // Kline close time  ~
#     "s": "BNBBTC",  // Symbol ~
#     "i": "1m",      // Interval
#     "f": 100,       // First trade ID
#     "L": 200,       // Last trade ID
#     "o": "0.0010",  // Open price  ~
#     "c": "0.0020",  // Close price  ~
#     "h": "0.0025",  // High price  ~
#     "l": "0.0015",  // Low price  ~
#     "v": "1000",    // Base asset volume  ~
#     "n": 100,       // Number of trades
#     "x": false,     // Is this kline closed?  ?
#     "q": "1.0000",  // Quote asset volume  ~
#     "V": "500",     // Taker buy base asset volume
#     "Q": "0.500",   // Taker buy quote asset volume
#     "B": "123456"   // Ignore
#   }
# }
