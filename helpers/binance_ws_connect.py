
import asyncio
import json
import websockets
import pandas as pd
import mplfinance as mpf


async def binance_websocket():
    uri = "wss://stream.binance.us:9443/ws/btcusdt@kline_1s"
    price_df = pd.DataFrame(columns=["Timestamp", "Open", "High", "Low", "Close"]) 
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            data = json.loads(message)
            timestamp = pd.Timestamp.now()
            open_price = float(data["k"]["o"])
            high_price = float(data["k"]["h"])
            low_price = float(data["k"]["l"])
            close_price = float(data["k"]["c"])
            
            new_row = pd.DataFrame({
                "Timestamp": [timestamp],
                "Open": [open_price],
                "High": [high_price],
                "Low": [low_price],
                "Close": [close_price]
            })
            
            price_df = pd.concat([price_df, new_row], ignore_index=True)
            
            plotted_df = price_df.copy()
            plotted_df['Timestamp'] = pd.to_datetime(plotted_df['Timestamp'])
            plotted_df.set_index('Timestamp', inplace=True)
            
            # Plot the candlestick chart without blocking script execution
            mpf.plot(plotted_df, type='candle', style='binance')
            
            print(f"Latest Close Price: {close_price}")            
            
asyncio.run(binance_websocket())


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
